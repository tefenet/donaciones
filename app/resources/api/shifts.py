from flask import jsonify, request, current_app as app, abort
from app.models.shifts import Shifts
from app.models.center import Center
from werkzeug.exceptions import BadRequestKeyError
from datetime import date, datetime
from pymysql import escape_string as thwart
from app.resources.shifts import get_end_time, create_shift


def index():
    # falta paginar y autenticar
    shifts = Shifts.all()
    shifts = list(map(lambda i: i.serialize(), shifts))
    return jsonify(shifts=shifts)


def avalaible_by_date(id):
    try:
        fecha = datetime.strptime(request.args['fecha'], '%Y-%m-%d').date()
    except BadRequestKeyError:
        fecha = date.today()
    except ValueError:
        return abort(500)
    center = Center.get_by_id(id)
    turnos = center.get_shifts_blocks_avalaible(fecha)
    if turnos:
        lista_turnos = []
        for start_time in turnos:
            end_time = get_end_time(start_time)
            turno = {
                "centro_id": id, "hora_inicio": start_time.isoformat(), "hora_fin": end_time.isoformat(),
                "fecha": fecha.isoformat()
            }
            lista_turnos.append(turno)

        dic = {'turnos': lista_turnos}
        return jsonify(dic)
    # si no hay turnos devuelve 500
    return abort(500)


def check_end_time(start_time, end_time):
    difference = end_time - start_time
    seconds_in_day = 24 * 60 * 60
    mins = divmod(difference.days * seconds_in_day + difference.seconds, 60)[0]
    if mins != 30:
        raise ValueError("Franja horaria de turno no válida. El turno debe ser de 30 minutos.")


def create(id):
    try:
        datos_turno = request.json
        fecha = datetime.strptime(datos_turno['fecha'], '%Y-%m-%d').date()
        email_donante = thwart(datos_turno['email_donante'])
        telefono_donante = thwart(datos_turno['telefono_donante'])
        hora_inicio = datetime.strptime(datos_turno['hora_inicio'], '%H:%M').time()
        hora_fin = datetime.strptime(datos_turno['hora_fin'], '%H:%M').time()

        center = Center.get_by_id(id)  # datos_turno['centro_id']
        check_end_time(datetime.strptime(datos_turno['hora_inicio'], '%H:%M'),
                       datetime.strptime(datos_turno['hora_fin'], '%H:%M'))

        if not center:
            return abort(500)

        params = {'donor_email': email_donante, 'donor_phone': telefono_donante,
                  'start_time': hora_inicio, 'date': fecha, 'center': center}
        if create_shift(params):
            return jsonify({
                "atributos": {"centro_id": id, "email_donante": email_donante, "telefono_donante": telefono_donante,
                              "hora_inicio": hora_inicio.isoformat(), "hora_fin": hora_fin.isoformat(),
                              "fecha": fecha.isoformat()}
            })
        return abort(500)
    except (BadRequestKeyError, ValueError) as err:
        app.logger.info(err)
        return abort(500)

    # consultar cuando devolver 400 error, si hay algún caso además de intentar acceder por GET
