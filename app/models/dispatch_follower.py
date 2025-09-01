# models/dispatch_follower.py
from app import db
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class DispatchFollower(db.Model):
    __tablename__ = 'dispatch_followers'
    dispatch_id = db.Column(PG_UUID(as_uuid=True), db.ForeignKey('dispatches.dispatch_id'), primary_key=True)
    user_id = db.Column(PG_UUID(as_uuid=True), primary_key=True)
    followed_at = db.Column(db.DateTime, nullable=False)

    dispatch = db.relationship('Dispatch', back_populates='followers')