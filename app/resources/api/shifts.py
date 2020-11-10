from flask import jsonify, request, current_app as app
from app.models.shifts import get_end_time, create_shift, check_end_time, check_date, str_date_to_datetime, \
    str_time_to_datetime
from app.models.center import Center
from app.models.shifts import Shifts
from werkzeug.exceptions import BadRequestKeyError
from datetime import date, datetime
import traceback


def get_json_turnos(turnos, fecha, centro_id):
    turnos_disp = []
    for start_time in turnos:
        end_time = get_end_time(start_time)
        turno = {
            "centro_id": centro_id, "hora_inicio": start_time.isoformat(), "hora_fin": end_time.isoformat(),
            "fecha": fecha.isoformat()
        }
        turnos_disp.append(turno)
    dic = {'turnos': turnos_disp}
    return jsonify(dic)


def get_json_error_msg(error_msg, error_code, status="error", **kwargs):
    """Retorna una tupla con un mensaje de error en formato json, y su coodigo de error"""
    return jsonify({'error': [
        {'status': status, 'error_msg': error_msg, 'error_code': error_code, **kwargs}]}), error_code


def avalaible_by_date(id):
    """Devuelve los turnos disponibles para el centro x. Parametro opcional: fecha. Si no recibe fecha, fecha=actual.
    """
    try:
        fecha = datetime.strptime(request.args['fecha'], '%Y-%m-%d').date()
    except BadRequestKeyError:  # no se recibe la fecha
        app.logger.info(traceback.format_exc())

        fecha = date.today()
    except ValueError:
        app.logger.info(traceback.format_exc())
        return get_json_error_msg(error_msg="formato de fecha no válido", error_code=422)
    except Exception as e:
        app.logger.info(traceback.print_exc())
        return get_json_error_msg(error_code=500, error_msg="Error en el servidor", status="internal server error")

    center = Center.get_by_id(id)
    if not center:
        return get_json_error_msg(error_msg="centro id={} inexistente".format(id), error_code=422)

    turnos = center.get_shifts_blocks_avalaible(fecha)
    if turnos:
        return get_json_turnos(turnos, fecha, center.id), 200

    return get_json_error_msg(center_info={"centro_id": center.id, "fecha": fecha.isoformat()},
                              status="shifts not available", error_code=200,
                              error_msg="no hay turnos disponibles".format(center.id))


def create(id):
    try:
        datos_turno = request.get_json()
        center = Center.get_by_id(id)  # datos_turno['centro_id']
        check_date(str_date_to_datetime(datos_turno['fecha']).date())
        check_end_time(str_time_to_datetime(datos_turno['hora_inicio']), str_time_to_datetime(datos_turno['hora_fin']))
        if not center:
            return get_json_error_msg(error_code=500, error_msg="id de centro no válido", status="center not found")

        datos_turno['hora_inicio'] = str_time_to_datetime(datos_turno['hora_inicio']).time()
        datos_turno['hora_fin'] = str_time_to_datetime(datos_turno['hora_fin']).time()
        datos_turno['fecha'] = str_date_to_datetime(datos_turno['fecha']).date()
        shift = Shifts.populate_from_api(datos_turno)
        created_shift = create_shift(shift, center)  # errores posibles capturados
        return jsonify({"atributos": created_shift.serialize()})
    except (BadRequestKeyError, ValueError, KeyError, AttributeError) as err:
        app.logger.info(traceback.format_exc())
        return get_json_error_msg(error_msg=str(err), error_code=420, status="invalid request")
    except Exception as e:
        app.logger.info(traceback.format_exc())
        return get_json_error_msg(error_code=500, error_msg="Error inesperado",
                                  status="internal server error")
