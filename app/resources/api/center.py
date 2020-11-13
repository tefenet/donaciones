from flask import jsonify, request
from app import dbSession
from app.models.center import Center
from app.models.sistema import Sistema
from sqlalchemy.orm.exc import NoResultFound


def show(center_id):
	"""retorna en formato JSON los datos del centro de ayuda solicitado en caso de estar publicamente disponible"""
	try:
		center = Center.get_by_id(center_id)
	except NoResultFound as error_message:
		return jsonify({'error': [
			{'status': 'Not Found', 'error_msg': str(error_message), 'error_code': 404}]}), 404
	if not center.published:
		return jsonify({'error': [
			{'status': 'Not Found', 'error_msg': 'no existe un centro con id %d' % center_id, 'error_code': 404}]}), 404
	return center.to_json()


def index():
	"""retorna en formato JSON los datos de todos los centros de ayuda publicados en el sitio"""
	cant_pagina = Sistema.get_sistema().cant_por_pagina
	#paginar segun la variable del sistema
	return "ruta de centro index (GET)"


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
		return new_center.to_json("atributos"), 201
	except:
		return jsonify(error_code=500, error_msg="Error inesperado", status="internal server error"), 500


