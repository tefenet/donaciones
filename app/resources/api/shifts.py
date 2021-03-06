from flask import jsonify, request, current_app as app
from sqlalchemy.orm.exc import NoResultFound

from app.helpers.formatter import str_time_to_datetime, str_date_to_datetime
from app.models.center import Center
from app.models.shifts import Shifts
from werkzeug.exceptions import BadRequestKeyError
from datetime import date, datetime
import traceback


def get_json_turnos(turnos, fecha, centro_id):
    turnos_disp = []
    for start_time in turnos:
        end_time = Shifts.get_end_time(start_time)
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
        center = Center.get_by_id(id)
        # fecha2 = datetime.strptime("2020-12-13", '%Y-%m-%d').date()
        # if fecha == fecha2:
        #     return get_json_error_msg(center_info={"centro_id": center.id, "fecha": fecha.isoformat()},
        #                               status="shifts not available", error_code=404,
        #                               error_msg="no hay turnos disponibles".format(center.id))
        if center.published is False:
            raise ValueError(
                "centro id={} no se encuentra activo".format(center.id))  # podria implementarse en el metodo
    except (ValueError, NoResultFound, BadRequestKeyError) as e:
        app.logger.info(traceback.format_exc())
        msg, error_code = str(e), 404
        if type(e) == BadRequestKeyError:
            msg, error_code = "error: fecha no recibida", 422
        return get_json_error_msg(error_msg=msg, error_code=error_code)

    except Exception as e:
        app.logger.info(traceback.print_exc())
        return get_json_error_msg(error_code=500, error_msg="Error en el servidor", status="internal server error")

    turnos = center.get_shifts_blocks_avalaible(fecha)
    if turnos:
        return get_json_turnos(turnos=turnos, fecha=fecha, centro_id=center.id), 200
    return get_json_error_msg(center_info={"centro_id": center.id, "fecha": fecha.isoformat()},
                              status="shifts not available", error_code=404,
                              error_msg="no hay turnos disponibles".format(center.id))


def create(id):
    try:
        datos_turno = request.get_json()
        if id != datos_turno['centro_id']:
            raise ValueError("id url no coincide con centro_id.")
        center = Center.get_by_id(id)  # datos_turno['centro_id']
        Shifts.check_date(str_date_to_datetime(datos_turno['fecha']).date())
        Shifts.check_duration(str_time_to_datetime(datos_turno['hora_inicio']),
                              str_time_to_datetime(datos_turno['hora_fin']))
        datos_turno['hora_inicio'] = str_time_to_datetime(datos_turno['hora_inicio']).time()
        datos_turno['hora_fin'] = str_time_to_datetime(datos_turno['hora_fin']).time()
        datos_turno['fecha'] = str_date_to_datetime(datos_turno['fecha']).date()
        shift = Shifts.populate_from_api(datos_turno)
        created_shift = Shifts.create_shift(shift, center)  # errores posibles capturados
        return jsonify({"atributos": created_shift.serialize()}), 200

    except (BadRequestKeyError, ValueError, KeyError, AttributeError, NoResultFound) as err:
        app.logger.info(traceback.format_exc())
        return get_json_error_msg(error_msg=str(err), error_code=420, status="invalid request")

    except Exception as e:
        app.logger.info(traceback.format_exc())
        return get_json_error_msg(error_code=500, error_msg="Error inesperado",
                                  status="internal server error")
