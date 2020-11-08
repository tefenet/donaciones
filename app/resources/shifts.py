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


def valid_start_time(start_time):
    """Chequeo que el horario del turno pertenezca a un horario válido"""
    return True if (time(9, 00) <= start_time <= time(15, 30)) else False


def get_end_time(start_time):
    t1 = datetime.strptime(str(start_time), '%H:%M:%S')
    t2 = datetime.strptime(str(time(0, 30)), '%H:%M:%S')
    time_zero = datetime.strptime(str(time(0)), '%H:%M:%S')
    return (t1 - time_zero + t2).time()


# @restricted(perm='shifts_new')
def create_shift(params):
    """Recibe center, donor_email, donor_phone, start_time, date.
    Retorna Boolean."""
    try:
        if valid_start_time(params['start_time']):
            center = params['center']
            end_time = get_end_time(params['start_time'])
            shift = Shifts(donor_email=params['donor_email'], donor_phone=params['donor_phone'],
                           start_time=params['start_time'], end_time=end_time, shift_date=params['date'],
                           center_id=params['center'].id)

            shifts_day = center.get_shifts_by_date(params['date'])
            if shifts_day:
                if shift_avalaible(shift.start_time, shifts_day):
                    raise ValueError("Error turno no disponible")

            dbSession.add(shift)
            dbSession.commit()
            return True
        raise ValueError("Franja horaria de turno no válida. El turno debe respetar la franja horaria de 9hs a 16hs.")

    except KeyError as err:
        raise ValueError("Error al obtener el parametro {}".format(err))


#####
# Create
@restricted(perm='user_new')
def new_view(center_id, date1=date.today()):
    center = Center.get_by_id(center_id)
    date1 = date(2020, 11, 3)
    if center:
        form = CreateShiftForm()

        # form.date.data = date1
        # choices_blocks = list(map(lambda d: (i, str(d)), get_shifts_blocks_avalaible(center_id, date1)))
        # choices_blocks = [(i + 1, str(d)) for i, d in enumerate(get_shifts_blocks_avalaible(center_id, date1))]

        return render_template("shifts/new.html", form=form, center=center, shift_date=date1)
    flash("Error al obtener el centro id={}".format(center_id))
    return redirect(url_for("turnos_index"))


@restricted(perm='shifts_new')
def create_view(center_id):
    """Recibe el id del centro al que pertenece el turno. Crea un turno siempre
    y cuando haya disponibilidad en el día elegido."""
    date1 = date(2020, 11, 3)
    center = Center.get_by_id(center_id)
    form = CreateShiftForm()
    date1 = form.date.data
    # form['start_time'] = QuerySelectField("Horario",
    #                                       query_factory=center.data.get_shifts_blocks_avalaible(form.date.data))
    # form.start_time.choices = center.get_shifts_blocks_avalaible(date1)

    if form.validate() and center:
        start_time = datetime.strptime(form.start_time.data, '%H:%M:%S').time()
        params = {'donor_email': thwart(form.donor_email.data), 'donor_phone': thwart(form.donor_phone.data),
                  'start_time': start_time, 'date': date1, 'center': center}
        try:
            create_shift(params)
            flash("Turno agregado exitosamente", "success")
        except ValueError as err:
            app.logger.info(params)
            flash(err, "danger")

    if not center:
        flash("Error al obtener el Centro con ID {}".format(center_id), "success")
    if form.errors:
        app.logger.info('por aqui pasó el aguila')
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
        res = paginate(Shifts.query_shifts_between(date_start, date_end), page, sys.cant_por_pagina)  # check User.query
    except AttributeError as err:  # AttributeError raise when page<1
        app.logger.info(err)
        return redirect(url_for('turnos_index'))
    return render_template("shifts/index.html", pagination=res, date_start=date_start, date_end=date_end, shifts=shifts)


def search_by_donor_email_paginated(donor_email, page=1):
    """Retorna una paginación con los usuarios que contengan username en su nombre de usuario"""
    sys = Sistema.get_sistema()
    query = Shifts.query_donor_email(donor_email)
    return paginate(query, page, sys.cant_por_pagina)


@restricted(perm='shifts_search')
def search_by_donor_email():
    """Busca turnos por email donante.
    Recibe email, que es un string, devuelve una lista de turnos(Shifts) """
    try:
        donor_email = request.args['donor_email']
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
    app.logger.info(query.all())
    app.logger.info("-------")
    return paginate(query, page, sys.cant_por_pagina)


@restricted(perm='shifts_search')
def search_by_center_name():
    """Busca turnos por nombre de centro.
    Recibe center_name(string), y numero de pagina, devuelve un template de lista de turnos(Shifts)"""
    try:
        center_name = request.args['center_name']
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError) as e:
        flash("ERROR: {}".format(e), e)
        return redirect(url_for('turnos_index'))

    try:
        pagination = search_by_center_name_paginated(center_name, page)
    except AttributeError:  # raised when page < 1
        page = 1
        pagination = search_by_center_name_paginated(center_name, page)
    return render_template("shifts/index.html", pagination=pagination, shifts=True, center_name=center_name)


def update_form():
    form_date = request.args['date']
    center = Center.get_by_id(request.args['center_id'])
    d = datetime.strptime(form_date, "%Y-%m-%d").date()
    return jsonify(list(map(lambda t: t.isoformat(), center.get_shifts_blocks_avalaible(d))))
