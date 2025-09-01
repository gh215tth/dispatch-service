# models/dispatch_processor.py
from app import db
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class DispatchProcessor(db.Model):
    __tablename__ = 'dispatch_processors'
    dispatch_id = db.Column(PG_UUID(as_uuid=True), db.ForeignKey('dispatches.dispatch_id'), primary_key=True)
    user_id = db.Column(PG_UUID(as_uuid=True), primary_key=True)
    assigned_at = db.Column(db.DateTime, nullable=False)
    deadline = db.Column(db.DateTime)

    dispatch = db.relationship('Dispatch', back_populates='processors')
