from flask_mail import Message, Mail

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
