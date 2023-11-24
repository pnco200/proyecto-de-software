from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from src.core.database import db

class User(db.Model):
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), unique=False)
    lastname = db.Column(db.String(50), unique=False)
    username = db.Column(db.String(50), unique=True)
    is_confirmed = db.Column(db.Boolean, unique=False, default=False)
    is_active = db.Column(db.Boolean, unique=False, default=True)
    confirm_token = db.Column(db.String(255), unique=False, default=None)
    password = db.Column(db.String(255))
    is_google = db.Column(db.Boolean, unique=False, default=False)
    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at= db.Column(db.DateTime, default=datetime.utcnow)
      
    

class Institution(db.Model):
    __tablename__= "institutions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True)
    information = db.Column(db.String(250), unique=False)
    address = db.Column(db.String(250), unique=False)
    localization =  db.Column(ARRAY(db.String(50)), unique=False)
    web = db.Column(db.String(250), unique=False)
    keywords = db.Column(db.String(500), unique=False)
    attention_time = db.Column(db.String(250), unique=False)
    contact = db.Column(db.String(250), unique=False)
    services = db.relationship('Service', back_populates='institution')
    is_active = db.Column(db.Boolean, unique=False)
    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at= db.Column(db.DateTime, default=datetime.utcnow)

        
class Rol(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at= db.Column(db.DateTime, default=datetime.utcnow)

class RolUsuario(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True)
    institution_id = db.Column(db.Integer, db.ForeignKey('institutions.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at= db.Column(db.DateTime, default=datetime.utcnow)


class Permiso(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at= db.Column(db.DateTime, default=datetime.utcnow)

class RolPermiso(db.Model):
    __tablename__ = 'permission_role'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'))

    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at= db.Column(db.DateTime, default=datetime.utcnow)
