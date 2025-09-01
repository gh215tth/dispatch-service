# models/dispatch_view.py
from app import db
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from datetime import datetime
import uuid

class DispatchView(db.Model):
    __tablename__ = 'dispatch_views'
    view_id = db.Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    dispatch_id = db.Column(PG_UUID(as_uuid=True), db.ForeignKey('dispatches.dispatch_id'), nullable=False)
    user_id = db.Column(PG_UUID(as_uuid=True), nullable=False)
    viewed_at = db.Column(db.DateTime, nullable=False)

    dispatch = db.relationship('Dispatch', back_populates='views')
