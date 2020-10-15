from flask import session, url_for, flash, redirect, abort, render_template
from functools import wraps


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if authenticated(session):
            return f(*args, **kwargs)
        else:
            flash("Tenes estar logueado para acceder a esta página!")
            return redirect(url_for('login'))  # url_login

    return wrap


def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if administrator(session):
            return f(*args, **kwargs)
        else:
            abort(401)

    return wrap


def authenticated(session):
    return session.get('logged_in')


def administrator(session):
    if ('user' in session) and (session['user'].tipo_cuenta == 1):
        return True
    return False


def clear_session(session):
    [session.pop(key) for key in list(session.keys()) if key != '_flashes']
