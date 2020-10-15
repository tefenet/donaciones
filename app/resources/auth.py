from flask import redirect, render_template, request, url_for, session, flash, current_app as app
from app.helpers.auth import authenticated, login_required, clear_session
from app.resources.forms import LoginForm
from app.models.user import User
from pymysql import escape_string as thwart


def set_session(user):
    """Recibe un usuario y setea los distintos campos de la sesión"""

    session['user_id'] = user.id
    session['user_email'] = user.email
    session['username'] = user.username
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

    params = request.form

    username = thwart(params['username']).lower()
    password = thwart(params['password'])

    user = User.query.filter(
        User.email == username).first()  # primero compruebo el que exista el correo, sino voy por el nombre de usuario

    if user is not None:
        if user.check_password(password) is False:  # pregunto si la pw conincide con el hash almacenado
            flash("Usuario/Email o Clave incorrecto.", "danger")
            return redirect(url_for('login'))
    else:
        user = User.query.filter(User.username == username).first()
        if user is None:
            flash("Usuario/Email o Clave incorrecto.", "danger")
            return redirect(url_for('login'))
        else:
            if user.check_password(password) is False:
                flash("Usuario/Email o Clave incorrecto.", "danger")
                return redirect(url_for('login'))
        if not user.active:
            flash("La cuenta que has ingresado está desactivada.", "danger")
            return redirect(url_for('login'))

    app.logger.info("user: %s", user)
    set_session(user)

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))

    set_session(user)
    app.logger.info("session %s", session)
    flash("La sesión se inició correctamente.")

    return redirect(url_for("home"))


@login_required
def logout():
    """El decorador @login_required lo uso para indicar que para acceder a esta ruta tengo que estar logueado.
    La función logout limpia la sesion y envía al usuario al home."""
    session.clear()
    clear_session()  # otra forma de limpiar la sesión puede ser recorriendo los items de la sesion y eliminarlos, similar al metodo session.clear() pero implementado por nosotros
    flash("La sesión se cerró correctamente.", "success")
    return redirect(url_for('home'))
