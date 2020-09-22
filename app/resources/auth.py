from flask import redirect, render_template, request, url_for, abort, session, flash, current_app as app
from app.db import dbSession
from app.models.user import User


def login():
    return render_template("auth/login.html")


def authenticate():
    params = request.form
    user = dbSession.query(User).filter(User.email == params["email"],
                                        User.password == params["password"]).first()  # query and
    app.logger.info("user: %s", user)

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))

    session["user"] = user.email
    app.logger.info("session %s", session)
    flash("La sesión se inició correctamente.")

    return redirect(url_for("home"))


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))
