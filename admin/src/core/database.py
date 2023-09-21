from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from src.core.test.test import Test

def init_app(app):
    db.init_app(app)
    config_db(app)

def config_db(app):
    @app.teardown_request
    def close_session(exception=None):
        db.session.close()

def reset_db():
    print("Resetting database...")
    db.drop_all()
    db.create_all()
