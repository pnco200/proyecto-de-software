from src.core.database import db
from src.core.institutions import Institution
from src.core.model.model import User,Rol,RolUsuario,RolPermiso,Permiso
from sqlalchemy import or_


def create_rol(**kwargs):
    """Crea un rol

    Args:
        **kwargs: Campos del rol

    Returns:
        Rol: Devuelve el rol creado
    """
    rol = Rol(**kwargs)
    db.session.add(rol)
    db.session.commit()
    return rol

def create_permission(**kwargs):
    """Crea un permiso

    Args:
        **kwargs: Campos del permiso
    
    Returns:
        Permiso: Devuelve el permiso creado
    """
    permission = Permiso(**kwargs)
    db.session.add(permission)
    db.session.commit()
    return permission

def create_rol_permission(**kwargs):
    """Crea un permiso para un rol

    Args:
        **kwargs: Campos del permiso para un rol
    
    Returns:
        RolPermiso: Devuelve el permiso creado para el rol
    """
    kwargs["role_id"] = get_role_id_by_name(kwargs["role_id"])
    kwargs["permission_id"] = get_permission_id_by_name(kwargs["permission_id"])
    permission_role = RolPermiso(**kwargs)
    db.session.add(permission_role)
    db.session.commit()
    return permission_role
    
        
def create_rol_usuario(**kwargs):
    """Crea un rol para un usuario

    Args:
        **kwargs: Campos del rol para un usuario
    
    Returns:
        RolUsuario: Devuelve el rol creado para el usuario
    """
    kwargs["role_id"] = get_role_id_by_name(kwargs["role_id"])
    user_role = RolUsuario(**kwargs)
    db.session.add(user_role)
    db.session.commit()
    return user_role

def get_roles_for_user(user_id, institution_id):
    """ Retorna los roles de un usuario en una institucion

    Args:
        user_id (_int_): user id
        institution_id (_int_): institution id

    Returns:
        list(RolUsuario): lista de roles del usuario en la institucion
    """
    user_roles = (
        db.session.query(RolUsuario.role_id)
        .filter(RolUsuario.user_id == user_id)
        .filter(RolUsuario.institution_id == institution_id)
        .all()
    )
    return [role.role_id for role in user_roles]

def get_rol_usuario(institution_id, user_id, role_name):
    """ Retorna el rol de un usuario en una institucion

    Args:
        user_id (_int_): user id
        institution_id (_int_): institution id
        role_name (_str_): nombre del rol
    
    Returns:
        list: lista de roles del usuario en la institucion
    """
    role_id = get_role_id_by_name(role_name)
    user_role = (
        db.session.query(RolUsuario)
        .filter(RolUsuario.user_id == user_id)
        .filter(RolUsuario.institution_id == institution_id)
        .filter(RolUsuario.role_id == role_id)
        .all()
    )
    return user_role

def get_user_admin_or_operator_in_institution(institution_id, user_id):
    """ Retorna los roles de administrador u operador de un usuario en una institucion
    
    Args:
        user_id (_int_): user id
        institution_id (_int_): institution id
    
    Returns:
        list: Lista de roles que el usuario tiene en la institución especificada.
    """
    roles = (
        db.session.query(Rol)
        .join(RolUsuario, RolUsuario.role_id == Rol.id)
        .filter(RolUsuario.user_id == user_id)
        .filter(RolUsuario.institution_id == institution_id)
        .filter(or_(RolUsuario.role_id == 2, RolUsuario.role_id == 4))        
        .all()
    )
    return roles

def delete_permission(permission_id):
    """Elimina un permiso

    Args:
        permission_id (_int_): id del permiso
    
    Returns:
        bool: True si se elimino el permiso, False en caso contrario
    """
    permission = Permiso.query.get(permission_id)
    if permission:
        db.session.delete(permission)
        db.session.commit()
        return True
    return False

def delete_rol_permission(role_id, permission_id):
    """Elimina un permiso de un rol

    Args:
        role_id (_int_): id del rol
        permission_id (_int_): id del permiso
    
    Returns:
        bool: True si se elimino el permiso del rol, False en caso contrario
    """
    role_permission = RolPermiso.query.filter_by(role_id=role_id, permission_id=permission_id).first()
    if role_permission:
        db.session.delete(role_permission)
        db.session.commit()
        return True
    return False

def delete_rol_usuario(user_id,institution_id, role_id):
    """ Elimina un rol de un usuario en una institucion

    Args:
        user_id (_int_): user id
        institution_id (_int_): institution id
        role_id (_int_): role id
    
    Returns:
        bool: True si se elimino el rol del usuario en la institucion, False en caso contrario

    """
    user_role = RolUsuario.query.filter_by(user_id=user_id, institution_id=institution_id, role_id=role_id).first()
    if user_role:
        db.session.delete(user_role)
        db.session.commit()
        return True
    return False

def get_role_id_by_name(role_name):
    """Retorna el id del rol segun el nombre

    Args:
        role_name (_str_): nombre del rol

    Returns:
        int: id del rol

    """
    print(role_name)
    rol = Rol.query.filter_by(name=role_name).first()
    return rol.id 


def get_permission_id_by_name(permission_name):
    """Retorna el id del permiso segun el nombre

    Args:
        permission_name (_str_): nombre del permiso
    
    Returns:
        int: id del permiso

    """
    permission = Permiso.query.filter_by(name=permission_name).first()
    return permission.id

def is_superadmin(user_id):
    """ Verifica si el usuario es superadmin

    Args:
        user_id (_int_): user id
    
    Returns:
        bool: True si es superadmin, False en caso contrario
    """
    role = (
        db.session.query(Permiso.name)
        .join(RolUsuario, RolUsuario.role_id == 3)
        .filter(RolUsuario.user_id == user_id)
        .all()
    )
    if role:
        return True
    else:
        return False
    
def is_institution_owner(user_id, institution_id):
    """Verifica si el usuario es dueño de la institucion

    Args:
        user_id (_int_): user id
        institution_id (_int_): institution id
    
    Returns:
        bool: True si es dueño, False en caso contrario

    """
    owner = (
        db.session.query(Permiso.name)
        .join(RolUsuario, RolUsuario.role_id == 1)
        .filter(RolUsuario.user_id == user_id)
        .filter(RolUsuario.institution_id == institution_id)
        .all()
    )
    if owner:
        return True
    else:
        return False
    
def list_institutions_owned_by_user(user_id):
    """Retorna las instituciones donde el user es dueño

    Args:
        user_id (int): user id

    Returns:
        list(Institutions): lista de instituciones donde el user es dueño
    """
    print(user_id)
    institutions = (
        db.session.query(Institution)
        .join(RolUsuario, RolUsuario.role_id == 1)
        .filter(RolUsuario.user_id == user_id)
        .filter(Institution.id == RolUsuario.institution_id)
        .all()
    )
    print(institutions)
    return institutions

def list_permissions_by_user_id(user_id):
    """ Obtener los permisos de un usuario

    Args:
        user_id (_int_): user id
    
    Returns:
        list: lista de permisos del usuario
    """
    permissions = (
        db.session.query(Permiso.name)
        .join(RolPermiso, RolPermiso.permission_id == Permiso.id)
        .join(RolUsuario, RolUsuario.role_id == RolPermiso.role_id)
        .filter(RolUsuario.user_id == user_id)
        .all()
    )

    # Extraer los nombres de los permisos de la consulta
    permission_names = [permission.name for permission in permissions]
    return permission_names

def list_Permissions_By_User_Id_In_Institution(user_id,institution_id):
    """ Obtener los permisos de un usuario en una institucion

    Args:
        user_id (_int_): user id
        institution_id (_int_): institution id
    
    Returns:
        list: lista de permisos del usuario en la institucion
    """
    permissions = (
        db.session.query(Permiso.name)
        .join(RolPermiso, RolPermiso.permission_id == Permiso.id)
        .join(RolUsuario, RolUsuario.role_id == RolPermiso.role_id)
        .filter(RolUsuario.user_id == user_id)
        .filter(RolUsuario.institution_id == institution_id)
        .all()
    )

    # Extraer los nombres de los permisos de la consulta
    permission_names = [permission.name for permission in permissions]

    return permission_names

