from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import dbSession

from app.models.sistema import Sistema
from app.models.user import User
from app.helpers.auth import login_required, restricted, is_not_admin
from app.helpers.handler import display_errors
from app.resources.forms import CreateUserForm, EditUserForm
from werkzeug.exceptions import BadRequestKeyError
from pymysql import escape_string as thwart
from sqlalchemy.exc import IntegrityError
from app.helpers.pagination import paginate


@restricted(perm='user_update')
def activate(user):
    user.activate()
    flash("El usuario {} fue activado exitosamente".format(user.email), "success")
    return True


@restricted(perm='user_update')
@is_not_admin()
def deactivate(user):
    user.deactivate()
    flash("El usuario {} fue desactivado exitosamente".format(user.email), "success")
    return True


@restricted(perm='user_find')
def find_by_username_paginated(username, page=1):
    """Retorna una paginación con los usuarios que contengan username en su nombre de usuario"""
    sys = Sistema.get_sistema()
    query = User.query_by_username(username)
    return paginate(query, page, sys.cant_por_pagina)


@restricted(perm='user_find')
def find_by_status_paginated(status=True, page=1):
    """Retornauna paginación con los usuarios con el estado recibido"""
    query = User.query_by_status(status)
    sys = Sistema.get_sistema()
    return paginate(query, page, sys.cant_por_pagina)


# Protected resources

#####
# Index
@restricted(perm='user_index')
def index():
    sys = Sistema.get_sistema()
    try:
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError):
        page = 1
    try:
        res = paginate(User.query, page, sys.cant_por_pagina)  # check User.query
    except AttributeError:  # AttributeError raise when page<1
        return redirect(url_for('user_index'))
    return render_template("user/index.html", pagination=res)


#####
# Create
@restricted(perm='user_new')
def new():
    form = CreateUserForm()
    return render_template("user/new.html", form=form)


@restricted(perm='user_new')
def create():
    """ Da de alta un usuario en la base de datos."""
    form = CreateUserForm(request.form)
    if form.validate():
        user = User(email=thwart(form.email.data), username=thwart(form.username.data),
                    first_name=thwart(form.first_name.data), last_name=thwart(form.last_name.data),
                    active=form.active.data)
        user.set_roles(list(form.user_roles.data))
        user.set_password(thwart(form.password.data))  # envio la pw para guardar el hash en la db.
        dbSession.add(user)
        dbSession.commit()
    if form.errors:
        display_errors(form.errors)  # si hay errores redirecciona a la pagina de crear usuario y muestra los errores.
        return redirect(url_for("user_new"))

    return redirect(url_for("user_index", page=1))


#####
# Update user

@restricted(perm='user_update')
def update_user_render(object_id):
    user = User.get_by_id(object_id)
    if user:
        form = EditUserForm(obj=user)
        return render_template('user/update.html', form=form, user_id=object_id)
    abort(500, "ERROR: Error al obtener usuario. id = {}".format(object_id))


@restricted(perm='user_update')
def update_user(object_id):
    form = EditUserForm(request.form)
    if form.validate():
        u = User.get_by_id(object_id)
        if u:
            u.update(email=thwart(form.email.data), username=thwart(form.username.data),
                     first_name=thwart(form.first_name.data), last_name=thwart(form.last_name.data))
            if form.password.data != '':
                u.set_password(thwart(form.password.data))
            if form.active.data != u.active:
                activate(u) if form.active.data else deactivate(u)
            u.set_roles(list(form.user_roles.data))
            try:
                u.updated()
                dbSession.commit()
            except IntegrityError:
                flash("Ya existe un usuario con ese correo/username", "danger")
                return render_template('user/update.html', form=form, user_id=object_id)
            flash("Usuario {} actualizado exitosamente.".format(u.username), "success")
            return redirect(url_for("user_index"))
    if form.errors:
        display_errors(
            form.errors)  # si hay errores redirecciona a la pagina de crear usuario y muestra los errores.
    flash("Error al validar formulario", "danger")
    return redirect(url_for("user_index"))


#####
# Deactivate user accounts

@restricted(perm='user_update')
def deactive_account(user_id=None):
    """Recibe un id de usuario. Si el usuario existe y su estado es activo,
     desactiva la cuenta seteando el campo active a False."""
    user = User.get_by_id(user_id)
    if user and user.active:
        deactivate(user)
        user.updated()
        dbSession.commit()
        return redirect(url_for("user_index"))
    abort(500, "ERROR: Error al obtener usuario. id = {}".format(user_id))
    return redirect(url_for("user_index", page=1))


@restricted(perm='user_update')
def activate_account(user_id=None):
    """Recibe un id de usuario. Si el usuario existe y su estado es inactivo,
     activa la cuenta seteando el campo active a True."""
    user = User.get_by_id(user_id)
    if user and user.active is False:
        activate(user)
        user.updated()
        dbSession.commit()
        return redirect(url_for("user_index"))
    abort(500, "ERROR: Error al obtener usuario. id = {}".format(user_id))
    return redirect(url_for("user_index", page=1))


#####
# Delete User

@restricted(perm='user_destroy')
@is_not_admin()
def __delete(user):
    """Elimina un usuario del sistema de manera definitiva.
    Retorna True si pudo eliminar el usuario, caso contrario retorna false"""
    if User.delete_by_id(user.id):
        dbSession.commit()
    return True


@restricted(perm='user_destroy')
def delete_user():
    try:
        user_id = request.args['object_id']
        u = User.get_by_id(user_id)
        if __delete(u):
            flash("Usuario id {} eliminado exitosamente".format(user_id), "success")
    except BadRequestKeyError:
        flash("ERROR: id usuario no recibido", "danger")
        return redirect(url_for('user_index'))
    except PermissionError:
        flash("ERROR: No podés eliminar a un usuario administrador!".format())
    return redirect(url_for('user_index'))


#####
# Search users

@restricted(perm='user_find')
def search_by_status():
    """Busca usuarios por estado(activo/inactivo).
    Recibe status, que es un booleano, devuelve una lista de usuarios """
    try:
        status = False if request.args['status'] == "False" else True
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError) as e:
        flash("ERROR: {}".format(e), e)
        return redirect(url_for('user_index'))

    try:
        pagination = find_by_status_paginated(status, page)
    except AttributeError:  # raised when page < 1
        page = 1
        pagination = find_by_status_paginated(status, page)
    return render_template("user/index.html", pagination=pagination)


@restricted(perm='user_find')
def search_by_username():
    """Busca usuarios por nombre de usuario.
    Recibe status, que es un booleano, devuelve una lista de usuarios """
    try:
        username = request.args['username']
        page = int(request.args['page'])
    except (BadRequestKeyError, ValueError) as e:
        flash("ERROR: {}".format(e), e)
        return redirect(url_for('user_index'))

    try:
        pagination = find_by_username_paginated(username, page)
    except AttributeError:  # raised when page < 1
        page = 1
        pagination = find_by_username_paginated(username, page)
    return render_template("user/index.html", pagination=pagination)


#####
# Profile page
@login_required
def profile():
    if session['user_id']:
        user = User.get_by_id(session['user_id'])
        return render_template("user/show.html", user=user)
    abort(502, "Error al obtener datos del perfil")
#####
