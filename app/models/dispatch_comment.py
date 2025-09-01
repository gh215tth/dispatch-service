# models/dispatch_comment.py
from app import db
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from datetime import datetime
import uuid

class DispatchComment(db.Model):
    __tablename__ = 'dispatch_comments'
    comment_id = db.Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    dispatch_id = db.Column(PG_UUID(as_uuid=True), db.ForeignKey('dispatches.dispatch_id'), nullable=False)
    author_user_id = db.Column(PG_UUID(as_uuid=True), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    dispatch = db.relationship('Dispatch', back_populates='comments')