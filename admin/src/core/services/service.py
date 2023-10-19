from sqlalchemy.dialects.postgresql import ARRAY

from datetime import datetime
from src.core.database import db
from enum import Enum

class TipoDeServicio(Enum):
    ANALISIS = "Análisis"
    CONSULTORIA = "Consultoría"
    DESARROLLO = "Desarrollo"

class Service(db.Model):
    __tablename__= "services"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=False)
    description = db.Column(db.String(255), unique=False)
    key_words = db.Column(ARRAY(db.String(50)), unique=False)
    centers = db.Column(ARRAY(db.String(50)), unique=False)
    type = db.Column(db.Enum(TipoDeServicio), nullable=False, default=TipoDeServicio.ANALISIS)
    enabled = db.Column(db.Boolean, unique=False, default=True)
    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id'))
    institution = db.relationship('Institution', back_populates='services')
    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at= db.Column(db.DateTime, default=datetime.utcnow)