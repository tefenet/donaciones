from os import environ
from flask import Flask, render_template
from flask_session import Session

from app.models import center, city, shifts
from config import config
from app.db import dbSession, init_db
from app.resources import issue, center, user, auth, sistema, shifts
from app.resources.api import issue as api_issue
from app.resources.api import shifts as api_shifts
from app.helpers import handler
from app.helpers import auth as helper_auth
from app.models.sistema import Sistema as Sys
from app.resources.sistema import Sistema
import importlib


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
    app.jinja_env.globals.update(has_perm=auth.user_has_permission)
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
    app.add_url_rule("/usuarios/editar/<int:object_id>", "user_update_by_id", user.update_user_render)
    app.add_url_rule("/usuarios/editar/<int:object_id>", "user_update_by_id_post", user.update_user, methods=["POST"])

    # Rutas de Centros
    app.add_url_rule("/center", "center_index", center.index)
    app.add_url_rule("/center", "center_create", center.create, methods=['POST'])
    app.add_url_rule("/center/new", "center_new", center.new)
    app.add_url_rule("/center/delete", "center_delete", center.delete_center, methods=["POST"])
    app.add_url_rule("/center/edit/<int:object_id>", "center_update_form", center.update_center_form)
    app.add_url_rule("/center/edit/<int:object_id>", "center_update", center.update_center, methods=["POST"])
    app.add_url_rule("/center/publish", "center_publish", center.toogle_publish_center, methods=["POST"])
    app.add_url_rule("/center/searchByName", "centro_search_by_name", center.search_by_name)
    app.add_url_rule("/center/searchByState", "centro_search_by_state", center.search_by_state)
    app.add_url_rule("/center/searchByPublished", "centro_search_by_published", center.search_by_published)
    app.add_url_rule("/center/approve", "center_approve", center.approve_center, methods=["POST"])
    app.add_url_rule("/center/reject", "center_reject", center.reject_center, methods=["POST"])
    app.add_url_rule("/center/review", "center_review", center.review_center, methods=["POST"])
    app.add_url_rule("/center/protocol/<int:object_id>", "get_protocol", center.get_protocol)

    # Rutas de Turnos
    app.add_url_rule("/turnos", "turnos_index", shifts.index)
    app.add_url_rule("/turnos/new/<int:center_id>", "turnos_new", shifts.new_view)
    app.add_url_rule("/turnos/create/<int:center_id>", "turnos_create", shifts.create_view, methods=["POST"])
    app.add_url_rule("/turnos/search_by", "turnos_search_by_donor", shifts.search_by_donor_email)
    app.add_url_rule("/turnos/search_by_cn", "turnos_search_by_center_name", shifts.search_by_center_name)
    app.add_url_rule("/turnos/deleteById", "turnos_delete_by_id", shifts.delete_shift, methods=["POST"])  # recibe id(int)
    app.add_url_rule("/cmd", "update_form", shifts.update_form)
    # app.add_url_rule("/turnos/choices", "get_choices", center.)

    # Rutas de Sistema
    app.add_url_rule("/sistema/configurar", "system_configure", sistema.config_sistema_get)
    app.add_url_rule("/sistema/configurar", "system_configure_post", sistema.config_sistema_post)

    # app.add_url_rule("/usuarios", "system_configure", user.index)
    # app.add_url_rule("/usuarios", "system", user.index)

    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        return render_template("home.html")

    # Session -- la agregué para ver la session desde el navegador en debug. Sí, es innecesaria.
    # @app.route('/session') ESTA RUTA NO TIENE SENTIDO
    # @helper_auth.restricted('session_show')
    # def get_session():
    #     return render_template('session.html', session=session)

    # Rutas de API-rest v1.0
    # api issue
    app.add_url_rule("/api/consultas", "api_issue_index", api_issue.index)

    # api shifts
    app.add_url_rule("/api/v1.0/turnos", "api_shifts_index", api_shifts.index)

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
