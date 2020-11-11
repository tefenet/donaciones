from flask import jsonify
from app.models.center import Center
from sqlalchemy.orm.exc import NoResultFound


def center_to_json(center):
	"""Convierte un centro de ayuda a formato JSON"""
	center_data = {
		"nombre": center.name, "direccion": center.address, "telefono": center.phone,
		"hora_apertura": center.opening.isoformat(), "hora_cierre": center.closing.isoformat(), "tipo": center.type,
		"web": center.web_site, "email": center.email}
	result = {'centro': center_data}
	return jsonify(result)


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
	return center_to_json(center)


def index():
	"""retorna en formato JSON los datos de todos los centros de ayuda publicados en el sitio"""
	#paginar segun la variable del sistema
	return "ruta de centro index (GET)"


def create():
	"""crea un nuevo centro de ayuda"""
	return "ruta de centro create (POST)"
