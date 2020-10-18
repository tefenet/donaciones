from flask import redirect, render_template, request, url_for, session, abort, flash, current_app as app
from app.db import dbSession
from app.models.user import User
from app.models.sistema import Sistema
from app.helpers.auth import login_required, admin_required, administrator
from app.helpers.handler import display_errors
from app.resources.forms import SistemaForm
from pymysql import escape_string as thwart


@admin_required
def config_sistema_get():
    sistema = Sistema.get_sistema()
    form = SistemaForm(obj=sistema)
    return render_template("sistema/config-sistema.html", form=form)


@admin_required
def config_sistema_post():
    form = SistemaForm(formdata=request.form)
    if form.validate_on_submit() and request.method == "POST":

        sistema = Sistema.get_sistema()
        sistema.titulo = thwart(form.titulo.data)
        sistema.descripcion = thwart(form.descripcion.data)
        sistema.bienvenida = thwart(form.bienvenida.data)
        sistema.email = thwart(form.email.data)
        sistema.cant_por_pagina = form.cant_por_pagina.data
        sistema.habilitado = form.habilitado.data

        dbSession.commit()

        flash("Configuración actualizada correctamente!", "success")
        # return redirect(url_for(''))
    else:
        display_errors(form.errors)
        # return redirect(url_for())
    return redirect(url_for('system_configure'))
