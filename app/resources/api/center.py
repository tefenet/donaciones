from flask import jsonify
from app.models.center import Center



def index():
	return "ruta de centro index (GET)"

def show(centro_id):
	return "ruta de centro show (GET) centros/%d" %centro_id

def create():
	return "ruta de centro create (POST)"



