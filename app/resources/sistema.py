from flask import redirect, render_template, request, url_for, session, abort, flash, current_app as app
from app.db import dbSession
from app.models.user import User
from app.models.sistema import Sistema
from app.helpers.auth import login_required, admin_required, administrator
from app.helpers.handler import display_errors
from app.resources.forms import SistemaForm
from werkzeug.exceptions import BadRequestKeyError
from pymysql import escape_string as thwart


def config_sistema_get():
    sistema = Sistema.query.get(1)
    form = SistemaForm(obj=sistema)
    return render_template("sistema/config-sistema.html", form=form)

def config_sistema_post(id):
    form = SistemaForm(formdata=request.form)
    if form.validate_on_submit() and request.method == "POST":
            
            sistema = Sistema.query.get(id)
            
            sistema.titulo = form.titulo.data
            sistema.descripcion = form.descripcion.data
            sistema.bienvenida = form.bienvenida.data
            sistema.email = form.email.data
            sistema.cant_por_pagina = form.cant_por_pagina.data

            dbSession.commit()

            flash("Configuración actualizada correctamente!", "success")
            #return redirect(url_for(''))
    else:
        display_errors(form.errors)
        #return redirect(url_for())
    return redirect(url_for('home'))