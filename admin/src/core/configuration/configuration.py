from datetime import datetime

from src.core.database import db


class Configuration(db.Model):
    __tablename__= "configuration"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    rows_per_page = db.Column(db.Integer)
    contact_information = db.Column(db.String(50), unique=True)
    is_maintenance = db.Column(db.Boolean, unique=False, default=False)
    maintenance_message = db.Column(db.String(255))
    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
