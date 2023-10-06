from src.core.database import db


class Test(db.Model):
    """"Modelo Test en la base de datos"""
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)