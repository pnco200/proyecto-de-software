from flask import Flask, render_template
from src.web import error
from src.core import database
from src.web.config import config
from src.web import error
from src.web.controllers.test import test_bp
#from src.web.controllers.issues import issues

def create_app(env="development", static_folder="../../static"):
    app = Flask(__name__, static_folder=static_folder)
    print(config[env])
    app.config.from_object(config[env])

    database.init_app(app)

    app.register_blueprint(test_bp)

    @app.get("/")
    def home():
<<<<<<< Updated upstream
=======
        return render_template("home.html", user={"is_authenticated":False}) #Hay que mandarle si el usuario esta logeado o no
    
    @app.get("/sendmailtest")
    def mail_test():
        email_utils.send_email("Prueba",["nicolaspanico2002@gmail.com"],"Esto es una prueba. </br> Funciono?")
>>>>>>> Stashed changes
        return render_template("home.html")

    app.register_error_handler(404,error.not_found_error404)

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    return app