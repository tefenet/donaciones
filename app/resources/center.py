from flask import redirect, render_template, request, url_for, session, abort, flash, current_app as app
from werkzeug.exceptions import BadRequestKeyError

from app import dbSession
from app.helpers.auth import restricted
from app.helpers.handler import display_errors
from app.helpers.pagination import paginate
from app.models.center import Center
from app.models.sistema import Sistema
from app.resources.forms import CreateCenterForm


@restricted(perm='centro_index')
def index():
    sys = Sistema.get_sistema()
    try:
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError):
        page = 1
    try:
        res = paginate(Center.query, page, sys.cant_por_pagina)  # check User.query
    except AttributeError:  # AttributeError raise when page<1
        return redirect(url_for('center_index'))
    return render_template("center/index.html", pagination=res)


@restricted(perm='centro_new')
def new():
    form = CreateCenterForm()
    return render_template("center/new.html", form=form)


@restricted(perm='centro_new')
def create():
    """ Da de alta un usuario en la base de datos."""
    form = CreateCenterForm(request.form)
    if form.validate():
        center = Center()
        form.populate_obj(center)
        dbSession.add(center)
        dbSession.commit()
    if form.errors:
        display_errors(form.errors)  # si hay errores redirecciona a la pagina de crear usuario y muestra los errores.
        return redirect(url_for("center_new"))

    return redirect(url_for("center_index", page=1))


@restricted(perm='centro_destroy')
def delete_center():
    """Elimina un centro de manera definitiva"""
    try:
        center_id = request.args['center_id']
        center_name = Center.get_by_id(center_id).name
        if Center.delete_by_id(center_id):
            dbSession.commit()
            flash("el Centro {} ha sido borrado".format(center_name), "info")
    except BadRequestKeyError:
        flash("ERROR: id Centro no recibido", "danger")
    finally:
        return redirect(url_for('center_index'))