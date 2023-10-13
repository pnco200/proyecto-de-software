from flask import Flask, render_template, flash
from src.web import error
from src.core import database
from src.core import bcrypt
from src.web.config  import config
from src.web import error
from src.web.controllers.test import test_bp
from src.web.controllers.auth import auth_bp
from src.web.controllers.users import user_bp
from src.web.helpers import auth
from flask_session import Session
from src.core.email import email_utils
#from src.web.controllers.issues import issues

session = Session()

def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    # INICIAR DEPENDENCIAS
    session.init_app(app)
    database.init_app(app)
    bcrypt.init_app(app)
    email_utils.init_app(app)

    # BLUEPRINTS
    app.register_blueprint(test_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)

    # URLS
    @app.get("/")
    def home():
        return render_template("home.html") #Hay que mandarle si el usuario esta logeado o no
    
    @app.get("/sendmailtest")
    def mail_test():
        email_utils.send_email("Prueba",["ramagp00@gmail.com"],"Esto es una prueba. </br> Funciono?")
        return render_template("home.html")
    
    #ERRORS
    app.register_error_handler(404,error.not_found_error404)
    app.register_error_handler(401,error.unauthorized)

    # JINJA
    app.jinja_env.globals.update(is_authenticated = auth.is_authenticated)

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    return app