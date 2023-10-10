from datetime import datetime

from src.core.database import db


class Institution(db.Model):
    __tablename__= "institutions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True)
    information = db.Column(db.String(250), unique=False)
    direction = db.Column(db.String(250), unique=False)
    localization = db.Column(db.String(250), unique=False)
    web = db.Column(db.String(250), unique=False)
    keywords = db.Column(db.String(250), unique=False)
    attention_time = db.Column(db.String(250), unique=False)
    contact = db.Column(db.String(250), unique=False)
    is_active = db.Column(db.Boolean, unique=False, default=True)
    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at= db.Column(db.DateTime, default=datetime.utcnow)