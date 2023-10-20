from flask import Flask, render_template, url_for, request, redirect, session, abort
from src.web import error
from src.core import database, seeds
from src.core import bcrypt
from src.core.configuration import is_in_maintenance
from src.web.config  import config
from src.web import error
from src.web.controllers.auth import auth_bp
from src.web.controllers.users import user_bp
from src.web.controllers.configuration import config_bp
from src.web.controllers.institution import institution_bp
from src.web.controllers.permissions import permissions_bp
from src.web.controllers.services import service_bp
from src.web.api.institutions import api_institution_bp
from src.web.api.auth import api_auth_bp
from src.web.api.services import api_service_bp
from src.web.controllers.services_requests import srequest_bp
from src.web.helpers import auth
from src.web.helpers import utils
from src.web.helpers import permissions
from flask_session import Session
from src.core.email import email_utils
from src.core import institutions
#from src.web.controllers.issues import issues

_session = Session()

def create_app(env="production", static_folder="../../static"):
    from src.web.api.users import api_user_bp
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    # INICIAR DEPENDENCIAS
    _session.init_app(app)
    database.init_app(app)
    bcrypt.init_app(app)
    email_utils.init_app(app)
    # BLUEPRINTS
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(config_bp)
    app.register_blueprint(institution_bp)
    app.register_blueprint(permissions_bp)
    app.register_blueprint(service_bp)
    app.register_blueprint(srequest_bp)
    app.register_blueprint(api_service_bp)
    #API BLUEPRINTS
    app.register_blueprint(api_institution_bp)
    app.register_blueprint(api_user_bp)    
    app.register_blueprint(api_auth_bp)
    def get_user_institutions():
        return institutions.get_user_institutions(session.get("user"),utils.current_selected_institution())
    
    # URLS
    @app.get("/")
    def home():
        return render_template("home.html")
    
    @app.get("/sendmailtest")
    def mail_test():
        email_utils.send_email("Prueba",["ramagp00@gmail.com"],"Esto es una prueba. </br> Funciono?")
        return render_template("home.html")
    
    #ERRORS
    app.register_error_handler(404,error.not_found_error404)
    app.register_error_handler(401,error.unauthorized)
    app.register_error_handler(503,error.maintenance)

    # JINJA
    app.jinja_env.globals.update(is_authenticated = auth.is_authenticated)
    app.jinja_env.globals.update(get_user_institutions = get_user_institutions)
    app.jinja_env.globals.update(current_selected_institution = utils.current_selected_institution)
    app.jinja_env.globals.update(is_superadmin = permissions.is_superadmin)
    app.jinja_env.globals.update(is_institution_owner = permissions.is_institution_owner)
    
    @app.before_request
    def verify_maintenance():
        if not permissions.is_superadmin():
            if is_in_maintenance():
                abort(503)
   
    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.cli.command(name="seeddb")
    def seeddb():
        seeds.run()
        print("Seeds ejecutados")
    return app