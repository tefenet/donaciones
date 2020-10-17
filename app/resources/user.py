from flask import redirect, render_template, request, url_for, session, abort, flash, current_app as app
from app.db import dbSession
from app.models.user import User
from app.helpers.auth import login_required, admin_required, administrator
from app.helpers.handler import display_errors
from app.resources.forms import CreateUserForm
from werkzeug.exceptions import BadRequestKeyError
from pymysql import escape_string as thwart


def is_administator(user_id):
    user = User.query.get(user_id)
    if user is None:
        return False
    return True if user.account_type == 1 else False


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
    if form.validate():
        user = User(email=thwart(form.email.data), username=thwart(form.username.data),
                    first_name=thwart(form.first_name.data), last_name=thwart(form.last_name.data),
                    active=form.active.data)
        user.set_password(thwart(form.password.data))  # envio la pw para guardar el hash en la db.
        dbSession.add(user)
        dbSession.commit()
    if form.errors:
        display_errors(form.errors)  # si hay errores redirecciona a la pagina de crear usuario y muestra los errores.
        return redirect(url_for("user_new"))

    return redirect(url_for("user_index"))


@admin_required
def deactive_account(id=None):
    """Recibe un id de usuario. Si el usuario existe y su estado es activo, desactiva la cuenta seteando el campo active a False."""
    user = User.query.get(id)
    if user and user.active is True:
        if is_administator(user.id):
            flash("El usuario {} es un administrador".format(user.email), "danger")
            return redirect(url_for("user_index"))
        else:
            user.active = False
            user.updated()
            dbSession.commit()
            flash("El usuario {} fue desactivado exitosamente".format(user.email), "success")
            return redirect(url_for("user_index"))
    flash("Usuario con id {} no encontrado".format(id), "danger")
    return redirect(url_for("user_index"))


@admin_required
def activate_account(id=None):
    """Recibe un id de usuario. Si el usuario existe y su estado es inactivo, activa la cuenta seteando el campo active a True."""
    user = User.query.get(id)
    if user and user.active is False:
        if is_administator(user.id):
            flash("El usuario {} es un administrador".format(user.email), "danger")
            return redirect(url_for("user_index"))
        else:
            user.active = True
            user.updated()
            dbSession.commit()
            flash("El usuario {} fue activado exitosamente".format(user.email), "success")
            return redirect(url_for("user_index"))
    flash("Usuario con id {} no encontrado".format(id), "danger")
    return redirect(url_for("user_index"))


@admin_required
def update_user(id=None):
    pass


@admin_required
def search_by_status():
    """Busca usuarios por estado(activo/inactivo).
    Recibe status, que es un booleano, devuelve una lista de usuarios """
    try:
        status = False if request.args['status'] == "False" else True
    except BadRequestKeyError:
        return render_template("user/index.html", users=[])
    users = list(User.query.filter(User.active == status))
    return render_template("user/index.html", users=users)


@admin_required
def search_by_username():
    """Busca usuarios por nombre de usuario.
    Recibe status, que es un booleano, devuelve una lista de usuarios """
    app.logger.info(request.form)
    try:
        username = request.args['username']
    except BadRequestKeyError:
        return render_template("user/index.html", users=[])

    users = list(User.query.filter(User.username.contains(username)))
    return render_template("user/index.html", users=users)


@login_required
def profile():
    if session['user_id']:
        return render_template("user/show.html", session=session)
    abort(502, "Error al obtener datos del perfil")
