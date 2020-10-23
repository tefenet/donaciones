from flask import redirect, render_template, request, url_for, session, abort, flash, current_app as app

from app import dbSession
from app.helpers.auth import restricted
from app.helpers.handler import display_errors
from app.models.center import Center
from app.resources.forms import CreateCenterForm


@restricted(perm='user_new')
def new():
    form = CreateCenterForm()
    return render_template("center/new.html", form=form)


@restricted(perm='user_new')
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
        return redirect(url_for("user_new"))

    return redirect(url_for("user_index", page=1))
