from os import environ
from flask import Flask, render_template, session
from flask_session import Session
from config import config
from app.db import dbSession, init_db
from app.resources import issue
from app.resources import user
from app.resources import auth
from app.resources import sistema
from app.resources.api import issue as api_issue
from app.helpers import handler
from app.helpers import auth as helper_auth
from app.models.sistema import Sistema as Sys
from app.resources.sistema import Sistema
import importlib
import pymysql


def create_app(environment="production"):
    # Configuración inicial de la app
    app = Flask(__name__)

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)


    """
    # conexion a la BD por pymsql
    def connection():
        db_conn = pymysql.connect(
            host=environ.get("DB_HOST", "localhost"),
            user=environ.get("DB_USER"),
            password=environ.get("DB_PASS"),
            db=environ.get("DB_NAME"),
            cursorclass=pymysql.cursors.DictCursor,
        )
        return db_conn
    """

    # Configure db, decorator cause callback cleanup, to release resources used by a session after request
    @app.teardown_appcontext
    def cleanup(resp_or_exc):
        dbSession.remove()

    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    app.jinja_env.globals.update(has_perm=auth.user_has_permission)
    app.jinja_env.globals.update(is_admin=helper_auth.administrator)
    app.jinja_env.globals.update(site_variables=Sys.get_sistema)



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
    app.add_url_rule("/usuarios/desactivar/<int:user_id>", "user_deactivate", user.deactive_account)
    app.add_url_rule("/usuarios/activar/<int:user_id>", "user_activate", user.activate_account)
    app.add_url_rule("/usuarios/perfil", "user_profile", user.profile)
    app.add_url_rule("/usuarios/buscarPorUsuario", "user_search_by_username",
                     user.search_by_username)  # recibe string(username)
    app.add_url_rule("/usuarios/buscarPorEstado", "user_search_by_status", user.search_by_status)  # recibe status(bool)
    app.add_url_rule("/usuarios/deleteById", "user_delete_by_id", user.delete_user, methods=["POST"])  # recibe id(int)
    app.add_url_rule("/usuarios/editar/<int:user_id>", "user_update_by_id", user.update_user_render)
    app.add_url_rule("/usuarios/editar/<int:user_id>", "user_update_by_id_post", user.update_user, methods=["POST"])

    # Rutas de Sistema
    app.add_url_rule("/sistema/configurar", "system_configure", sistema.config_sistema_get)
    app.add_url_rule("/sistema/configurar", "system_configure_post", sistema.config_sistema_post, methods=["POST"])

    # app.add_url_rule("/usuarios", "system_configure", user.index)
    # app.add_url_rule("/usuarios", "system", user.index)

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

    # Ruta de configuración del sistema
    app.add_url_rule("/sistema/config-sistema", 'config_sistema_get', sistema.config_sistema_get)
    app.add_url_rule("/sistema/actualizar-configuracion", 'config_sistema_post',
                     sistema.config_sistema_post, methods=["POST"])

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(500, handler.internal_server_error)

    # Implementar lo mismo para el error 500 y 401

    # import all models, context for flask_shell
    @app.shell_context_processor
    def make_shell_context():
        modules = dict(app=app)
        modelsmodule = importlib.import_module('app.models')
        for modulename in modelsmodule.__dict__:
            modules[modulename] = getattr(modelsmodule, modulename)
        modules['db'] = dbSession
        print('Modulos auto-importados ', [i[0] for i in modules.items()])
        return modules

    # Retornar la instancia de app configurada
    return app
