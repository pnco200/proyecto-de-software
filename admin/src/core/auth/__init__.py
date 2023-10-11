from src.core.database import db
from src.core.auth.user import User
from src.core.configuration import get_rows_per_page
from src.core.bcrypt import bcrypt
def list_users():
    return User.query.all()
    
def create_user(**kwargs):
    hash = bcrypt.generate_password_hash(kwargs["password"].encode('utf-8'))
    kwargs.update(password=hash.decode("utf-8"))
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
def find_user_by_username(username):
    """Encontrar usuario por nombre de usuario

    Args:
        username (_str_): nombre de usuario a buscar

    Returns:
        User: Devuelve usuario si lo encuentra
    """
    return User.query.filter_by(username=username).first()

def check_user(email,password):
    user = find_user_by_email(email)
    if user and bcrypt.check_password_hash(user.password, password.encode("utf-8")):
        return user
    else:
        return None
    
def confirm_email(token):
    user = User.query.filter_by(confirm_token=token).first()
    if user: 
        user.is_confirmed = True
        db.session.commit()
        return user  
    else:
        return None

def list_users_paged(page, only_blocked=None):
    per_page = get_rows_per_page()
    query = User.query

    if only_blocked is not None:
        query = query.filter_by(is_active=only_blocked)

    return query.paginate(page=page, per_page=per_page, error_out=False)

def change_user_status(user_id):
    """Change user status

    Args:
        user_id (integer): id of the user

    Returns:
        boolean: True if was changed, else False
    """
    user = User.query.filter_by(id=user_id).first()
    if(not user): ## TO DO--> ADD OR IF USER IS SUPER ADMIN
        return False
    user.is_active = not user.is_active
    db.session.commit()
    return True
