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
    

class UserRole(db.Model):
    __tablename__ = "user_roles"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    institucion = db.Column(db.Integer, db.ForeignKey('institucion_prueba'))

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True)
    permissions = db.relationship('Permission', secondary='role_permissions')

class RolePermission(db.Model):
    __tablename__ = "role_permissions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'))

class Permission(db.Model):
    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True)

class Institution(db.Model):
    __tablename__ = "institucion_prueba"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(255),unique=True)
  
    

