from flask import redirect, render_template, request, url_for, session, abort, flash, current_app as app
from app.db import dbSession
from app.models.sistema import Sistema
from app.models.shifts import Shifts
from app.models.center import Center
from app.helpers.auth import login_required, restricted, is_not_admin
from app.helpers.handler import display_errors
from app.resources.forms import CreateShiftForm
from werkzeug.exceptions import BadRequestKeyError
from pymysql import escape_string as thwart
from sqlalchemy.exc import IntegrityError
from app.helpers.pagination import paginate
from datetime import datetime, timedelta, date, time

shift_time_blocks = [time(9), time(9, 30), time(10), time(10, 30), time(11), time(11, 30), time(12), time(12, 30),
                     time(13), time(13, 30), time(14), time(14, 30), time(15), time(15, 30)]


def get_shifts_blocks_avalaible(center_id, date1=date.today()):
    """Retorna los bloques de horario disponibles para el día date1, para un centro dado"""

    center = Center.get_by_id(center_id)
    if center is None:
        raise ValueError("Error al obtener el centro id={}".format(center_id))
    shifts = center.get_shifts_by_date(date1)
    if shifts:
        not_avalaible = list(map(lambda s: (s.start_time if s.start_time in shift_time_blocks else None), shifts))
        return [t for t in shift_time_blocks if t not in not_avalaible]  # shift_time_blocks - not_avalaible
    return shift_time_blocks


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
                           start_time=params['start_time'], end_time=end_time, date=params['date'],
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
    # date1 = date(2020, 11, 3)
    if center:
        form = CreateShiftForm()
        form.date.data = date1
        # choices_blocks = list(map(lambda d: (i, str(d)), get_shifts_blocks_avalaible(center_id, date1)))
        # choices_blocks = [(i + 1, str(d)) for i, d in enumerate(get_shifts_blocks_avalaible(center_id, date1))]
        form.start_time.choices = get_shifts_blocks_avalaible(center_id, date1)
        return render_template("shifts/new.html", form=form, center=center, shift_date=date1)
    flash("Error al obtener el centro id={}".format(center_id))
    return redirect(url_for("turnos_index"))


@restricted(perm='shifts_new')
def create_view(center_id):
    """Recibe el id del centro al que pertenece el turno. Crea un turno siempre
    y cuando haya disponibilidad en el día elegido."""

    center = Center.get_by_id(center_id)

    form = CreateShiftForm(request.form)
    date1 = form.date.data
    form.start_time.choices = get_shifts_blocks_avalaible(center_id, date1)

    if form.validate() and center:
        start_time = datetime.strptime(form.start_time.data, '%H:%M:%S').time()
        params = {'donor_email': thwart(form.donor_email.data), 'donor_phone': thwart(form.donor_phone.data),
                  'start_time': start_time, 'date': date1, 'center': center}
        try:
            create_shift(params)
            flash("Turno agregado exitosamente", "success")
        except ValueError as err:
            flash(err, "danger")

    if not center:
        flash("Error al obtener el Centro con ID {}".format(center_id), "success")
    if form.errors:
        display_errors(form.errors)
        return redirect(url_for("turnos_new", center_id=center_id))

    return redirect(url_for("turnos_index", page=1))


@restricted(perm='shifts_index')
def index(date_start=date.today(), date_end=(datetime.now() + timedelta(2)).date()):
    shifts = Shifts.get_shifts_between()
    app.logger.info(shifts)
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
