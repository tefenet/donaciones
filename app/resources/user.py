from flask import redirect, render_template, request, url_for, session, abort
from app.db import dbSession
from app.models.user import User
from app.helpers.auth import authenticated


# Protected resources
def index():
    if not authenticated(session):
        abort(401)

    users = User.query.all()
    # User.query.filter(User.name == 'admin').first()
    return render_template("user/index.html", users=users)


def new():
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")


def create():
    if not authenticated(session):
        abort(401)

    args = list(request.form.values())
    user = User(email=args[0], password=args[1], first_name=args[2], last_name=args[3])
    dbSession.add(user)
    dbSession.commit()
    return redirect(url_for("user_index"))
