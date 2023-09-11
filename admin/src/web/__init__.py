from flask import Flask, render_template
from src.web import error


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return render_template("home.html")

    app.register_error_handler(404,error.not_found_error404)

    return app