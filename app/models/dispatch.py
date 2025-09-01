# app/models/dispatch.py
from app import db
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from datetime import datetime
import uuid

# Alembic/SQLAlchemy sẽ tạo enum types
security_enum = db.Enum('public', 'internal', 'confidential', name='security_level')
urgency_enum = db.Enum('normal', 'urgent', 'immediate', name='urgency_level')
status_enum = db.Enum('pending', 'in_progress', 'completed', 'archived', name='processing_status')

class Dispatch(db.Model):
    __tablename__ = 'dispatches'
    dispatch_id = db.Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_number = db.Column(db.String(100), nullable=False, unique=True)
    summary = db.Column(db.Text)
    page_count = db.Column(db.Integer)

    security_level = db.Column(security_enum, nullable=False)
    urgency_level = db.Column(urgency_enum, nullable=False)
    processing_status = db.Column(status_enum, nullable=False)

    document_type_id = db.Column(PG_UUID(as_uuid=True), db.ForeignKey('document_types.document_type_id'), nullable=False)
    issuing_body_id = db.Column(PG_UUID(as_uuid=True), db.ForeignKey('issuing_bodies.issuing_body_id'), nullable=False)

    creator_user_id = db.Column(PG_UUID(as_uuid=True), nullable=False)
    approver_user_id = db.Column(PG_UUID(as_uuid=True))

    arrival_timestamp = db.Column(db.DateTime)
    effective_timestamp = db.Column(db.DateTime)
    expiration_timestamp = db.Column(db.DateTime)
    approved_at = db.Column(db.DateTime)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    document_type = db.relationship('DocumentType', backref=db.backref('dispatches', lazy=True))
    issuing_body = db.relationship('IssuingBody', backref=db.backref('dispatches', lazy=True))

    recipients = db.relationship('DispatchRecipient', back_populates='dispatch', cascade="all, delete-orphan")
    processors = db.relationship('DispatchProcessor', back_populates='dispatch', cascade="all, delete-orphan")
    followers = db.relationship('DispatchFollower', back_populates='dispatch', cascade="all, delete-orphan")
    attachments = db.relationship('DispatchAttachment', back_populates='dispatch', cascade="all, delete-orphan")
    comments = db.relationship('DispatchComment', back_populates='dispatch', cascade="all, delete-orphan")
    views = db.relationship('DispatchView', back_populates='dispatch', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Dispatch {self.document_number}>"
