from os import environ
from flask import Flask, render_template, session
from flask_session import Session
from config import config
from app.db import dbSession, init_db
from app.resources import issue
from app.resources import user
from app.resources import auth
from app.resources.api import issue as api_issue
from app.helpers import handler
from app.helpers import auth as helper_auth


def create_app(environment="production"):
    # Configuración inicial de la app
    app = Flask(__name__)

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # Configure db, decorator cause callback cleanup, to release resources used by a session after request
    @app.teardown_appcontext
    def cleanup(resp_or_exc):
        dbSession.remove()

    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])

    # Rutas de Consultas
    app.add_url_rule("/consultas", "issue_index", issue.index)
    app.add_url_rule("/consultas", "issue_create", issue.create, methods=["POST"])
    app.add_url_rule("/consultas/nueva", "issue_new", issue.new)

    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)
    app.add_url_rule("/usuarios/desactivar/<int:id>", "user_deactivate", user.deactive_account)
    app.add_url_rule("/usuarios/activar/<int:id>", "user_activate", user.activate_account)
    app.add_url_rule("/usuarios/perfil", "user_profile", user.profile)

    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        return render_template("home.html")

    # Session
    @app.route('/session')
    @helper_auth.admin_required
    def get_session():
        return render_template('session.html', session=session)

    # Rutas de API-rest
    app.add_url_rule("/api/consultas", "api_issue_index", api_issue.index)

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(500, handler.internal_server_error)
    # Implementar lo mismo para el error 500 y 401

    # Retornar la instancia de app configurada
    return app
