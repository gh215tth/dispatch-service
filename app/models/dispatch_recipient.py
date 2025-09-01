# models/dispatch_recipient.py
from app import db
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class DispatchRecipient(db.Model):
    __tablename__ = 'dispatch_recipients'
    dispatch_id = db.Column(PG_UUID(as_uuid=True), db.ForeignKey('dispatches.dispatch_id'), primary_key=True)
    user_id = db.Column(PG_UUID(as_uuid=True), primary_key=True)
    notified_at = db.Column(db.DateTime)

    dispatch = db.relationship('Dispatch', back_populates='recipients')