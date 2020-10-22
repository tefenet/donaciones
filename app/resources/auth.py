from flask import redirect, render_template, request, url_for, session, flash, current_app as app
from app.helpers.auth import authenticated, login_required, clear_session, user_has_perm
from app.helpers.handler import display_errors
from app.resources.forms import LoginForm
from app.models.user import User
from app.models.sistema import Sistema
from pymysql import escape_string as thwart


def set_session(user):
    """Recibe un usuario y setea los distintos campos de la sesión"""

    session['user_id'] = user.id
    session['user_email'] = user.email
    session['username'] = user.username
    session['current_user'] = User.get_by_id(user.id)
    session['logged_in'] = True
    session['is_admin'] = True if (user.account_type == 1) else False
    session['perfil_activo'] = None


def login():
    if authenticated(session):
        flash("Ya tenes una sesión activa.", "warning")
        return redirect(url_for('home'))
    form = LoginForm()
    return render_template('auth/login.html', form=form)


def authenticate():
    """authenticate() realiza los chequeos necesarios para autorizar el ingreso del usuario al sistema.
    La funcion thwart del paquete pymsql se encarga de sanitizar el parametro para evitar posibles sql injections"""

    sis_config = Sistema.get_sistema()
    form = LoginForm(request.form)
    if form.validate():
        username = thwart(form.username.data.lower())
        password = thwart(form.password.data.lower())

        app.logger.info("username {}".format(username))

        user = User.query.filter(
            User.email == username).first()  # primero compruebo el que exista el correo, sino voy por el nombre de usuario
        if user is not None:
            if user.check_password(password) is False:  # pregunto si la pw conincide con el hash almacenado
                flash("Usuario/Email o Clave incorrecto.", "danger")
                return redirect(url_for('auth_login'))
        else:
            # si llegué aca es porque no encontro el mail, pruebo buscando el username
            user = User.query.filter(User.username == username).first()
            if user is None:
                flash("Usuario/Email o Clave incorrecto.", "danger")
                return redirect(url_for('auth_login'))
            else:
                if user.check_password(password) is False:
                    flash("Usuario/Email o Clave incorrecto.", "danger")
                    return redirect(url_for('auth_login'))

        if not user.active:
            flash("La cuenta que has ingresado se encuentra inactiva.", "danger")
            return redirect(url_for('auth_login'))

        if not sis_config.habilitado and not user.is_admin():
            flash("No puedes loguearte porque el sitio no esta disponible momentaneamente.", "danger")
            return redirect(url_for('home'))

        app.logger.info("user: %s", user)
        set_session(user)
        flash("La sesión se inició correctamente.", "success")
        return redirect(url_for("home"))

    if form.errors:
        display_errors(form.errors)
        return redirect(url_for("auth_login"))


@login_required
def logout():
    """El decorador @login_required lo uso para indicar que para acceder a esta ruta tengo que estar logueado.
    La función logout limpia la sesion y envía al usuario al home."""
    session.clear()
    # clear_session()  # otra forma de limpiar la sesión puede ser recorriendo los items de la sesion y eliminarlos, similar al metodo session.clear() pero implementado por nosotros
    flash("La sesión se cerró correctamente.", "success")
    return redirect(url_for('home'))


def user_has_permission(permission_name):
    if session and session.get('logged_in'):
        return user_has_perm(permission_name)
    return False
