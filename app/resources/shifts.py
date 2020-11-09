from datetime import datetime, timedelta, date, time

from flask import redirect, render_template, request, url_for, flash, current_app as app
from flask.json import jsonify
from pymysql import escape_string as thwart
from werkzeug.exceptions import BadRequestKeyError

from app.db import dbSession
from app.helpers.auth import restricted
from app.helpers.handler import display_errors
from app.helpers.pagination import paginate
from app.models.center import Center
from app.models.shifts import Shifts
from app.models.sistema import Sistema
from app.resources.forms import CreateShiftForm


def shift_avalaible(start_time, shifts_day):
    """Chequea si el turno esta disponible. Retorna un Boolean"""
    return list(filter(lambda s: s.start_time == start_time, shifts_day))


def get_end_time(start_time):
    t1 = datetime.strptime(str(start_time), '%H:%M:%S')
    t2 = datetime.strptime(str(time(0, 30)), '%H:%M:%S')
    time_zero = datetime.strptime(str(time(0)), '%H:%M:%S')
    return (t1 - time_zero + t2).time()


# @restricted(perm='shifts_new')
def create_shift(shift):
    """recibe un turno y lo valida antes de persistirlo."""
    center = Center.get_by_id(shift.center_id)
    if not center:
        flash("Error al obtener el Centro con ID {}".format(shift.center_id), "success")
    if center.valid_start_time(shift.start_time):
        available_start = center.get_shifts_blocks_avalaible(shift.date)
        if shift.start_time not in available_start:
            raise ValueError("Error: turno no disponible")
        shift.end_time = get_end_time(shift.start_time)
        dbSession.add(shift)
        dbSession.commit()
    else:
        raise ValueError("Franja horaria de turno no válida. El turno debe respetar la franja horaria de 9hs a 16hs.")


#####
# Create
@restricted(perm='shifts_new')
def new_view(center_id):
    center = Center.get_by_id(center_id)
    if center:
        form = CreateShiftForm()
        return render_template("shifts/new.html", form=form, center=center)
    flash("Error al obtener el centro id={}".format(center_id))
    return redirect(url_for("turnos_index"))


@restricted(perm='shifts_new')
def create_view(center_id):
    """Recibe el id del centro al que pertenece el turno. Crea un turno siempre
    y cuando haya disponibilidad en el día elegido."""
    form = CreateShiftForm()
    if form.validate():
        shift = Shifts()
        form.populate_obj(shift)
        shift.center_id = center_id
        try:
            create_shift(shift)
            flash("Turno agregado exitosamente", "success")
        except ValueError as err:
            flash(err, "danger")
    if form.errors:
        display_errors(form.errors)
        return redirect(url_for("turnos_new", center_id=center_id))
    return redirect(url_for("turnos_index", page=1))


@restricted(perm='shifts_index')
def index(date_start=date.today(), date_end=(datetime.now() + timedelta(2)).date()):
    shifts = Shifts.get_shifts_between()
    sys = Sistema.get_sistema()
    try:
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError):
        page = 1
    try:
        res = paginate(Shifts.query_shifts_between(date_start, date_end), page, sys.cant_por_pagina)
    except AttributeError as err:  # AttributeError raise when page<1
        app.logger.info(err)
        return redirect(url_for('turnos_index'))
    return render_template("shifts/index.html", pagination=res, date_start=date_start, date_end=date_end, shifts=shifts)


def search_by_donor_email_paginated(donor_email, page=1):
    """Retorna una paginación con los turnos que contengan donor_email"""
    sys = Sistema.get_sistema()
    query = Shifts.query_donor_email(donor_email)
    return paginate(query, page, sys.cant_por_pagina)


@restricted(perm='shifts_search')
def search_by_donor_email():
    """Busca turnos por email donante.
    Recibe email, que es un string, devuelve una lista de turnos(Shifts) """
    try:
        donor_email = thwart(request.args['donor_email'])
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError) as e:
        flash("ERROR: {}".format(e), e)
        return redirect(url_for('turnos_index'))
    try:
        pagination = search_by_donor_email_paginated(donor_email, page)
    except AttributeError:  # raised when page < 1
        page = 1
        pagination = search_by_donor_email_paginated(donor_email, page)
    return render_template("shifts/index.html", pagination=pagination, shifts=True, donor_email=donor_email)


def search_by_center_name_paginated(center_name, page=1):
    """Retorna una paginación con los turnos pertenecientes al centro 'center_name'"""
    sys = Sistema.get_sistema()
    query = Shifts.query_center_name(center_name)
    return paginate(query, page, sys.cant_por_pagina)


@restricted(perm='shifts_search')
def search_by_center_name():
    """Busca turnos por nombre de centro.
    Recibe center_name(string), y numero de pagina, devuelve un template de lista de turnos(Shifts)"""
    app.logger.info(request.args)
    try:
        center_name = thwart(request.args['center_name'])
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError) as e:
        flash("ERROR: {}".format(e), e)
        return redirect(url_for('turnos_index'))
    c = Center.get_by_name(center_name)
    try:
        pagination = search_by_center_name_paginated(c, page)
    except AttributeError:  # raised when page < 1
        page = 1
        pagination = search_by_center_name_paginated(c, page)
    return render_template("shifts/index.html", pagination=pagination, shifts=True, center_name=center_name)


def update_form():
    form_date = request.args['date']
    center = Center.get_by_id(request.args['center_id'])
    d = datetime.strptime(form_date, "%Y-%m-%d").date()
    return jsonify(list(map(lambda t: t.isoformat(), center.get_shifts_blocks_avalaible(d))))


@restricted(perm='shifts_destroy')
def __delete(shift):
    """Elimina un turno del sistema de manera definitiva.
    Retorna True si pudo eliminar el turno, caso contrario retorna false"""
    if Shifts.delete_by_id(shift.id):
        dbSession.commit()
    return True


@restricted(perm='shifts_destroy')
def delete_shift():
    try:
        shift_id = request.args['object_id']
        s = Shifts.get_by_id(shift_id)
        if __delete(s):
            flash("Turno id {} eliminado exitosamente".format(shift_id), "success")
    except BadRequestKeyError:
        flash("ERROR: shift_id no recibido", "danger")
        return redirect(url_for('turnos_index'))
    return redirect(url_for('turnos_index'))
