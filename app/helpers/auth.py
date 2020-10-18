from flask import session, url_for, flash, redirect, abort, render_template
from functools import wraps


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if authenticated(session):
            return f(*args, **kwargs)
        else:
            flash("Tenes estar logueado para acceder a esta página!")
            abort(401)

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


#aca hay que reemplazarlo haciendo el chequeo con el metodo del modelo
def administrator(session):
    if 'user_id' in session and session['is_admin']:
        return True
    return False


def clear_session(session):
    [session.pop(key) for key in list(session.keys()) if key != '_flashes']
