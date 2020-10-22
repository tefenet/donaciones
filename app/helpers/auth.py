from flask import session, url_for, flash, redirect, abort, render_template
from functools import wraps

from app.models.permission import Permission
from app.models.user import User


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


# aca hay que reemplazarlo haciendo el chequeo con el metodo del modelo
def administrator(session):
    if 'user_id' in session and session['is_admin']:
        return True
    return False


def clear_session(session):
    [session.pop(key) for key in list(session.keys()) if key != '_flashes']


def user_has_perm(permission_name):
    current_user = User.get_by_id(session.get('user_id'))
    perm = Permission.get_by_name(permission_name)
    return current_user.has_permission(perm)


def restricted(perm):
    def decorator(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if user_has_perm(perm):
                return f(*args, **kwargs)
            else:
                abort(401)

        return wrap

    return decorator
