from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import dbSession
from app.models.user import User
from app.helpers.auth import authenticated, admin_required
from app.helpers.handler import display_errors
from app.resources.forms import CreateUserForm
from pymysql import escape_string as thwart


# Protected resources
@admin_required
def index():
    users = User.query.all()
    return render_template("user/index.html", users=users)


@admin_required
def new():
    form = CreateUserForm()
    return render_template("user/new.html", form=form)


@admin_required
def create():
    """ Da de alta un usuario en la base de datos."""
    form = CreateUserForm(request.form)
    user = User(email=thwart(form.email.data), username=thwart(form.username.data),
                first_name=thwart(form.first_name.data), last_name=thwart(form.last_name.data), active=form.active.data)
    user.set_password(thwart(form.password.data))  # envio la pw para guardar el hash en la db.
    dbSession.add(user)
    dbSession.commit()
    if form.errors:
        display_errors(form.errors)  # si hay errores redirecciona a la pagina de crear usuario y muestra los errores.
        return url_for("new_user")

    return redirect(url_for("index"))


def deactive_account(id=None):
    """Recibe un id de usuario. Si el usuario existe desactiva la cuenta seteando el campo active a False."""
    user = User.query.get(id=id)
    if user and (user.active is True):
        user.active = False
        dbSession.commit()
        flash("El usuario {} fue desactivado exitosamente".format(user.email), "success")
    flash("Usuario con id {} no encontrado".format(id), "danger")
    return redirect(url_for("deactivate_account"))
