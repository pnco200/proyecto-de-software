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
    

class UserRole(db.model):
    __tablename__ = "user_roles"
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    institucion = db.Column(db.Integer, db.ForeignKey('roles.id'))

class Role(db.model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True)
    permissions = db.relationship('Permission', secondary='role_permissions')

class RolePermission(db.model):
    __tablename__ = "role_permissions"
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'))

class Permission(db.model):
    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True)

def list_permissions_by_user(user_id):
    # Hacer una consulta JOIN para obtener los permisos del usuario
    nombres_permisos = (
        db.session.query(Permission.name)
        .join(RolePermission, Role, UserRole)
        .filter(UserRole.user_id == user_id)
        .all()
    )

    #hacer una lista con solo los nombres de los permisos
    nombres_permisos = [name for name , in nombres_permisos]

    return nombres_permisos  