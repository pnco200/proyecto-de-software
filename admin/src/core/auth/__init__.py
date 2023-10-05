from src.core.database import db
from src.core.auth.user import User
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
    print(User.query.filter_by(email=email).first())
    return User.query.filter_by(email=email).first()

def check_user(email,password):
    user = find_user_by_email(email)
    if user and bcrypt.check_password_hash(user.password, password.encode("utf-8")):
        return user
    else:
        return None