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
from datetime import datetime, timedelta, date
import datetime as dt


def shift_avalaible(start_time, shifts_day):
    """Chequea si el turno esta disponible. Retorna un Boolean"""
    return list(filter(lambda s: s.start_time == start_time, shifts_day))


def valid_start_time(start_time):
    """Chequeo que el horario del turno pertenezca a un horario válido"""
    return True if (dt.time(9, 30) <= start_time <= dt.time(15, 30)) else False


def get_end_time(start_time):
    t1 = dt.datetime.strptime(str(start_time), '%H:%M:%S')
    t2 = dt.datetime.strptime(str(dt.time(0, 30)), '%H:%M:%S')
    time_zero = dt.datetime.strptime(str(dt.time(0)), '%H:%M:%S')
    return (t1 - time_zero + t2).time()


# @restricted(perm='shifts_new')
def create_shift(params):
    """Recibe center, donor_email, donor_phone, start_time, end_time, date.
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


@restricted(perm='shifts_new')
def create_shift_view(center_id):
    """Recibe el id del centro al que pertenece el turno. Crea un turno siempre
    y cuando haya disponibilidad en el día elegido."""

    form = CreateShiftForm(request.form)
    center = Center.get_by_id(center_id)
    if form.validate() and center:
        params = {'donor_email': thwart(form.donor_email.data), 'donor_phone': thwart(form.donor_phone.data),
                  'start_time': form.start_time.data, 'end_time': form.end_time.data, 'date': form.date.data,
                  'center': center}

        try:
            create_shift(params)
            flash("Turno agregado exitosamente", "success")
        except ValueError as err:
            flash(err, "danger")

    if not center:
        flash("Error al obtener el Centro con ID {}".format(center_id), "success")
    if form.errors:
        display_errors(form.errors)  # si hay errores redirecciona a la pagina de crear usuario y muestra los errores.
        return redirect(url_for("user_new"))

    return redirect(url_for("center ", page=1))


def index():
    shifts = Shifts.get_shifts_between()
    sys = Sistema.get_sistema()
    date_start = date.today()
    date_end = (datetime.now() + timedelta(2)).date()
    try:
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError):
        page = 1
    try:
        res = paginate(Shifts.query, page, sys.cant_por_pagina)  # check User.query
    except AttributeError:  # AttributeError raise when page<1
        return redirect(url_for('shifts_index'))
    return render_template("shifts/index.html", pagination=res, date_start=date_start, date_end=date_end, shifts=shifts)
