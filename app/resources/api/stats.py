import urllib
from calendar import monthrange
from collections import Counter
from itertools import chain

from flask import jsonify

from app.models.center import Center
from app.models.shifts import Shifts
from datetime import date
from json import loads


def get_json_error_msg(error_msg, error_code, status="error", **kwargs):
    """Retorna una tupla con un mensaje de error en formato json, y su coodigo de error"""
    return jsonify({'error': [
        {'status': status, 'error_msg': error_msg, 'error_code': error_code, **kwargs}]}), error_code


def get_cities_dict(api_url="https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios?page=1&per_page=150"):
    with urllib.request.urlopen(api_url) as url:
        data = loads(url.read().decode())
        d = {}
        for center in data["data"]["Town"].values():
            d[center['id']] = center['name']
    return d


def shifts_by_month(month):
    """Devuelve los turnos por ciudad para el mes indicado.
    """
    try:
        inicio_de_mes = date(2020, month, 1)
        fin_de_mes = date(2020, month, 30).replace(day=monthrange(2020, month)[1])
        shifts_of_month = Shifts.query_shifts_between(inicio_de_mes, fin_de_mes)
        city_names = get_cities_dict()
        city_counts = list(map(lambda sh: city_names[sh.center.city_id], shifts_of_month))
        return jsonify(Counter(city_counts))
    except ValueError as e:
        msg, error_code = str(e), 404
        return get_json_error_msg(error_msg=msg, error_code=error_code)
    except (OSError, ConnectionError) as e:
        return get_json_error_msg(error_code=500, error_msg="Error en el servidor", status="internal server error")


def shifts_by_city(city_id):
    """dada una ciudad Devuelve los turnos totales por tipo de centro de la ciudad indicada, recibe el id de la ciudad.
    """
    try:
        shifts_of_city = list(chain(*[c.shifts for c in Center.get_by_city(city_id)]))
        city_counts = list(map(lambda sh: sh.center.center_type, shifts_of_city))
        return jsonify(Counter(city_counts))
    except ValueError as e:
        msg, error_code = str(e), 404
        return get_json_error_msg(error_msg=msg, error_code=error_code)
    except (OSError, ConnectionError) as e:
        return get_json_error_msg(error_code=500, error_msg="Error en el servidor", status="internal server error")


def top_six_cities():
    """Devuelve las 6 ciudaes con mas turnos para centros de alimentos en este mes, y sus cantidades respectivas.no recibe parametros
        """
    today=date.today()
    inicio_de_mes = today.replace(day=1)
    fin_de_mes = today.replace(day=monthrange(2020, today.month)[1])
    shifts_of_month =list(filter(lambda sh: sh.center.center_type == 'alimentos', Shifts.query_shifts_between(inicio_de_mes, fin_de_mes)))
    city_names = get_cities_dict()
    city_counts = list(map(lambda sh: city_names[sh.center.city_id], shifts_of_month))
    return jsonify(dict(Counter(city_counts).most_common(6)))