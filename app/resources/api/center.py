from flask import jsonify, request
from app import dbSession
from app.models.center import Center
from app.models.sistema import Sistema
from app.helpers.pagination import Page
from sqlalchemy.orm.exc import NoResultFound


def show(center_id):
    """retorna en formato JSON los datos del centro de ayuda solicitado en caso de estar publicamente disponible"""
    try:
        center = Center.get_by_id(center_id)
    except NoResultFound as error_message:
        return jsonify({'error': [
            {'status': 'Not Found', 'error_msg': str(error_message), 'error_code': 404}]}), 404
    if not center.published:
        return jsonify({'error': [{'status': 'Invalid Request', 'error_msg':
        'El centro con id: %d no se encuentra disponible publicamente' % center_id, 'error_code': 420}]}), 420
    return jsonify({'centro': center.serialized()})


def index():
    """retorna en formato JSON los datos de todos los centros de ayuda publicados en el sitio"""
    cant_pagina = Sistema.get_sistema().cant_por_pagina
    if 'page' in request.args:
        page = int(request.args['page'])
    else:
        page = 1
    try:
        result = Page(Center.query_by_published(True), page, cant_pagina)
        total = result.pages()
        if page > total:
            raise ValueError('Pagina no valida')
    except (ValueError, AttributeError):
        return jsonify({'error': [{'status': 'Invalid Request', 'error_msg': 'Pagina no disponible',
                        'error_code': 420}]}), 420
    listado = []
    for center in result.items:
        center_serialized = center.serialized()
        listado.append(center_serialized)
    result = {
        'centros': listado,
        'total': total,
        'pagina': page,
    }
    return jsonify(result)


def create():
    """crea un nuevo centro de ayuda"""
    try:
        data = request.get_json()  #si el mimetype no indica JSON retorna None
        if data is None:
            return jsonify({'error': [
                {'status': 'Bad Request', 'error_msg': 'Solicitud no valida', 'error_code': 400}]}), 400
        new_center = Center()
        new_center.name = data['nombre']
        new_center.address = data['direccion']
        new_center.phone = data['telefono']
        new_center.opening = data['hora_apertura']
        new_center.closing = data['hora_cierre']
        new_center.type = data['tipo']
        new_center.web_site = data['web']
        new_center.email = data['email']
        dbSession.add(new_center)
        dbSession.commit()
        return jsonify({'atributos': new_center.serialized()}), 201
    except:
        return jsonify(error_code=500, error_msg="Error inesperado", status="internal server error"), 500


