from flask import redirect, render_template, request, url_for, session, abort, flash, current_app as app
from app.db import dbSession
from app.models.sistema import Sistema
from app.models.user import User
from app.helpers.auth import login_required, admin_required, administrator
from app.helpers.handler import display_errors
from app.resources.forms import CreateUserForm, EditUserForm
from werkzeug.exceptions import BadRequestKeyError
from pymysql import escape_string as thwart
from sqlalchemy.exc import IntegrityError
from app.helpers.pagination import paginate


def is_administator(user_id):
    user = User.get_by_id(user_id)
    if user is None:
        return False
    return user.is_admin()


# Protected resources
@admin_required
def index():
    sys = Sistema.get_sistema()
    page = int(request.args['page'])
    res = paginate(User.query, page, sys.cant_por_pagina)  # check User.query
    user_is_admin = is_administator(session['user_id'])
    return render_template("user/index.html", pagination=res, user_is_admin=user_is_admin)


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

    return redirect(url_for("user_index", page=1))


def activate(user):
    user.activate()
    flash("El usuario {} fue activado exitosamente".format(user.email), "success")
    return True


def deactivate(user):
    if not is_administator(user.id):
        user.deactivate()
        flash("El usuario {} fue desactivado exitosamente".format(user.email), "success")
        return True
    flash("Error al desactivar usuario. No podés desactivar a un administrador")
    return False


@admin_required
def deactive_account(id=None):
    """Recibe un id de usuario. Si el usuario existe y su estado es activo, desactiva la cuenta seteando el campo active a False."""
    user = User.get_by_id(id)
    if user and user.active:
        deactivate(user)
        user.updated()
        dbSession.commit()
        return redirect(url_for("user_index", page=1))
    flash("Usuario con id {} no encontrado".format(id), "danger")
    return redirect(url_for("user_index",page=1))


@admin_required
def activate_account(id=None):
    """Recibe un id de usuario. Si el usuario existe y su estado es inactivo, activa la cuenta seteando el campo active a True."""
    user = User.get_by_id(id)
    if user and user.active is False:
        activate(user)
        user.updated()
        dbSession.commit()
        return redirect(url_for("user_index",page=1))
    flash("Usuario con id {} no encontrado".format(id), "danger")
    return redirect(url_for("user_index", page=1))


@admin_required
def search_by_status():
    """Busca usuarios por estado(activo/inactivo).
    Recibe status, que es un booleano, devuelve una lista de usuarios """
    try:
        status = False if request.args['status'] == "False" else True
        page = int(request.args['page'])
        user_is_admin = is_administator(session['user_id'])
    except BadRequestKeyError: # no se que es este error pero la paginación es incorrecta
        return render_template("user/index.html", users=[])
    pagination = User.find_by_status_paginated(status, page)
    return render_template("user/index.html", pagination=pagination,user_is_admin=user_is_admin)


@admin_required
def search_by_username():
    """Busca usuarios por nombre de usuario.
    Recibe status, que es un booleano, devuelve una lista de usuarios """
    app.logger.info(request.form)
    try:
        username = request.args['username']
        page = int(request.args['page'])
        user_is_admin = is_administator(session['user_id'])
    except BadRequestKeyError: # no se que es este error pero la paginación es incorrecta
        return render_template("user/index.html", pagination=[])
    pagination = User.find_by_username_paginated(username, page)
    return render_template("user/index.html", pagination=pagination, user_is_admin=user_is_admin)


@login_required
def profile():
    if session['user_id']:
        user = User.get_by_id(session['user_id'])
        return render_template("user/show.html", user=user)
    abort(502, "Error al obtener datos del perfil")


@admin_required
def update_user_render(user_id):
    user = User.get_by_id(user_id)
    app.logger.info("entre")
    if user:
        form = EditUserForm(obj=user)
        return render_template('user/update.html', form=form, user_id=user_id)
    flash("ERROR: Error al obtener usuario", "danger")
    return redirect(url_for("user_index", page=1))


@admin_required
def update_user(user_id):
    form = EditUserForm(request.form)
    if form.validate():
        u = User.get_by_id(user_id)
        if u:
            u.update(email=thwart(form.email.data), username=thwart(form.username.data),
                     first_name=thwart(form.first_name.data), last_name=thwart(form.last_name.data))
            if form.password.data != '':
                u.set_password(thwart(form.password.data))
            if form.active.data != u.active:
                activate(u) if form.active.data else deactivate(u)
            try:
                u.updated()
                dbSession.commit()
            except IntegrityError:
                flash("Ya existe un usuario con ese correo/username", "danger")
                return render_template('user/update.html', form=form, user_id=user_id)
            flash("Usuario {} actualizado exitosamente.".format(u.username), "success")
            return redirect(url_for("user_index", page=1))
    if form.errors:
        display_errors(
            form.errors)  # si hay errores redirecciona a la pagina de crear usuario y muestra los errores.
    flash("Error al validar formulario", "danger")
    return redirect(url_for("user_index",page=1))


@admin_required
def __delete(id):
    """Elimina un usuario del sistema de manera definitiva.
    Retorna True si pudo eliminar el usuario, caso contrario retorna false"""
    u = User.get_by_id(id)
    if u and not u.is_admin():
        if User.delete_by_id(id):
            dbSession.commit()
            return True
    return False


@admin_required
def delete_user():
    try:
        user_id = request.args['user_id']
        if __delete(user_id):
            flash("Usuario id {} eliminado exitosamente".format(user_id), "success")
            return redirect(url_for('user_index'))
    except BadRequestKeyError:
        flash("ERRROR: id usuario no recibido", "danger")
        return redirect(url_for('user_index'))
    flash("Error el borrar usuario con id {}. No podés borrar a un administrador".format(user_id), "danger")
    return redirect(url_for('user_index'))
