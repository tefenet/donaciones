import urllib
from calendar import monthrange
from collections import Counter
from flask import jsonify
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
