from flask_mail import Message, Mail
from datetime import datetime
import uuid
mail = None

def init_app(app):
    """"Configurar variable para enviar mails"""
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'grupo25ps@gmail.com'
    app.config['MAIL_PASSWORD'] = 'wohq uqfa rfag pafz'

    global mail
    mail = Mail(app)

def send_confirmation_email(email : str):
    """"Envio de Mail de confirmacion"""
    try:
        token = str(uuid.uuid4())
        final_url = "https://admin-grupo25.proyecto2023.linti.unlp.edu.ar/auth/confirmemail?token=" + token
        message = Message("Mail de confirmacion para tu cuenta de CIDEPINT", recipients=[email])
        message.body = "Hola! Para terminar el registro, debes confirmar tu cuenta de CIDEPINT Clickea en el siguiente link para terminar el proceso: " + final_url
        message.sender = "Grupo CIDEPINT <grupo25ps@gmail.com>"
        mail.send(message)
        return token
    except Exception as e:
        print(str(e))
        return False

def send_email(subject : str, recipients : list, body : str):
    """"Envio de Mail"""
    message = Message(subject, recipients=recipients)
    message.body = body
    message.sender = "Grupo CIDEPINT <grupo25ps@gmail.com>"
    try:
        mail.send(message)
        return True
    except Exception as e:
        print(str(e))
        return False
