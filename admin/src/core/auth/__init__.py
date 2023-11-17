from src.core.database import db
from src.core.model.model import User, RolUsuario
from src.core.configuration import get_rows_per_page
from src.core.bcrypt import bcrypt
from src.core import rol_permission
def list_users():
    query = User.query

    subquery = db.session.query(RolUsuario.user_id).filter_by(role_id=3).subquery()
    
    query = query.filter(~User.id.in_(subquery))
    return query.all()
    
def create_user(**kwargs):
    """Crear usuario

    Args:
        **kwargs (_dict_): Diccionario con los datos del usuario a crear

    Returns:
        User: Devuelve usuario creado
    """
    hash = bcrypt.generate_password_hash(kwargs["password"].encode('utf-8'))
    kwargs.update(password=hash.decode("utf-8"))
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()
    return user

def create_user_google(**kwargs):
    """Crear usuario con google

    Args:
        **kwargs (_dict_): Diccionario con los datos del usuario a crear

    Returns:
        User: Devuelve usuario creado
    """
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()
    return user

def find_user_by_email(email):
    """Encontrar usuario por mail

    Args:
        email (_str_): Email del usuario a buscar

    Returns:
        User: Devuelve usuario si lo encuentra
    """
    return User.query.filter_by(email=email).first()

def find_user_by_id(id):
    return User.query.fileter_by(id=id).first()    


def find_user_by_username(username):
    """Encontrar usuario por nombre de usuario

    Args:
        username (_str_): nombre de usuario a buscar

    Returns:
        User: Devuelve usuario si lo encuentra
    """
    return User.query.filter_by(username=username).first()
def find_user_by_id(id):
    """Encontrar usuario por id

    Args:
        id (_int_): id del usuario a buscar

    Returns:
        User: Devuelve usuario si lo encuentra
    """
    return User.query.filter_by(id=id).first()

def check_user(email,password):
    """Verificar usuario por email y password

    Args:
        email (_str_): email del usuario
        password (_str_): password del usuario

    Returns:
        User: Devuelve usuario si la verificación es exitosa
        None: Devuelve None en caso contrario
    """
    user = find_user_by_email(email)

    if user and not user.is_google and bcrypt.check_password_hash(user.password, str(password).encode("utf-8")):
        return user
    else:
        return None
    
def confirm_email(token):
    """Confirmar email del usuario

    Args:
        token (_str_): token de confirmación
    
    Returns:
        User: Devuelve usuario si el token es correcto
        None: Devuelve None en caso contrario
    """
    user = User.query.filter_by(confirm_token=token).first()
    if user: 
        user.is_confirmed = True
        db.session.commit()
        return user  
    else:
        return None

def list_users_paged(page, only_blocked=None, email=None):
    """Listar usuarios en forma paginada

    Args:
        page (_int_): Número de página
        only_blocked (_bool_, optional): Si es True, lista solo usuarios bloqueados. Si es False, lista usuarios no bloqueados.
        email (_str_, optional): Filtra usuarios por dirección de correo electrónico.

    Returns:
        Pagination: Objeto paginado con la lista de usuarios.
    """
    per_page = get_rows_per_page()
    query = User.query
    if only_blocked is not None:
        query = query.filter_by(is_active=only_blocked)
    if email is not None:
        query = query.filter(User.email.ilike(f"%{email}%"))
    
    subquery = db.session.query(RolUsuario.user_id).filter_by(role_id=3).subquery()
    
    query = query.filter(~User.id.in_(subquery))

    return query.paginate(page=page, per_page=per_page, error_out=False)

def change_user_status(user_id):
    """Cambiar estado de usuario

    Args:
        user_id (_int_): Id del usuario 

    Returns:
        boolean: True si se cambió el estado, False en caso contrario
    """
    user = User.query.filter_by(id=user_id).first()
    if(not user): ## TO DO--> ADD OR IF USER IS SUPER ADMIN
        return False
    user.is_active = not user.is_active
    db.session.commit()
    return True

def assign_institution_owner(user_id, institution_id):
    """Asignar usuario como dueño de institución

    Args:
        user_id (_int_): Id del usuario
        institution_id (_int_): Id de la institución
    
    Returns:
        boolean: True si se asignó el usuario como dueño, False en caso contrario
    """
    rol_permission.create_rol_usuario(
        role_id = "Owner",
        user_id = user_id,
        institution_id = institution_id
    )
    return True


def delete_institution_owner(user_id, institution_id):
    """Eliminar usuario como dueño de institución

    Args:
        user_id (_int_): Id del usuario
        institution_id (_int_): Id de la institución
    
    Returns:
        boolean: True si se eliminó el usuario como dueño, False en caso contrario
    """
    ###TO DO
    ###borar la tabla de user_rol que tenga user_id e institution_id
    if rol_permission.delete_rol_usuario(user_id,institution_id, 1):
        return True
    else:
        return False

def assign_institution_member(user_id, permission_id, institution_id):
    """Asignar usuario como miembro de institución

    Args:
        user_id (_int_): Id del usuario
        permission_id (_int_): Id del permiso
        institution_id (_int_): Id de la institución
    
    Returns:
        boolean: True si se asignó el usuario como miembro, False en caso contrario
    """
    rol_permission.create_rol_usuario(
        role_id = permission_id,
        user_id = user_id,
        institution_id = institution_id
    )    
    return True


def delete_institution_member(user_id, permission_id, institution_id):
    """Eliminar usuario como miembro de institución
    
    Args:
        user_id (_int_): Id del usuario
        permission_id (_int_): Id del permiso
        institution_id (_int_): Id de la institución

    Returns:
        boolean: True si se eliminó el usuario como miembro, False en caso contrario
    """
    rol_permission.delete_rol_usuario(user_id,institution_id, permission_id)
    return True