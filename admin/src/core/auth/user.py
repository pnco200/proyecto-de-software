from datetime import datetime

from src.core.database import db


class User(db.Model):
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), unique=True)
    lastname = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    is_confirmed = db.Column(db.Boolean, unique=False, default=False)
    is_active = db.Column(db.Boolean, unique=False, default=True)
    confirm_token = db.Column(db.String(255), unique=False, default=None)
    password = db.Column(db.String(255))
    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at= db.Column(db.DateTime, default=datetime.utcnow)