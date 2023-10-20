from datetime import datetime
from src.core.database import db


class ServiceRequest(db.Model):
    __tablename__ = "service_request"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    state_id = db.Column(db.Integer, db.ForeignKey('service_state.id'))
    archive = db.Column(db.LargeBinary)    
    observations = db.Column(db.String(255), unique=False)
    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    closed_at=db.Column(
        db.DateTime, default=None
    )
    inserted_at= db.Column(db.DateTime, default=datetime.utcnow)


class ServiceState(db.Model):
    __tablename__ = "service_state"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=False)
    state_message = db.Column(db.String(255), unique=False)
    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at= db.Column(db.DateTime, default=datetime.utcnow)
    extend_existing=True


class ServiceRequestMessages(db.Model):
    __tablename__ = "service_request_messages"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    service_request_id = db.Column(db.Integer, db.ForeignKey('service_request.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    msg_content = db.Column(db.String(255), unique=False )
    updated_at=db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at= db.Column(db.DateTime, default=datetime.utcnow)
    