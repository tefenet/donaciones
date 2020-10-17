from flask import redirect, render_template, request, url_for
from app.db import dbSession
#from app.models.sistema import Sistema



def index():
	#aca se tiene que detectar si el sitio esta deshabilitado para mostrarlo distinto
	#obtener la tabla del sistema, tomar la columna de habilitado y enviarlo a la vista
	#system_config = Sistema.Query.all()
	return render_template("home.html")




