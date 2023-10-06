from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from src.core.test.test import Test
from src.core.auth.user import User

def init_app(app):
    """"Iniciar la base de datos"""
    db.init_app(app)
    config_db(app)

def config_db(app):
    """"Configuracion de la aplicacion"""
    @app.teardown_request
    def close_session(exception=None):
        db.session.close()

def reset_db():
    """"Reiniciar la base de datos"""
    print("Resetting database...")
    db.drop_all()
    db.create_all()
