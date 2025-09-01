# models/issuing_body.py
from app import db
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
import uuid

class IssuingBody(db.Model):
    __tablename__ = 'issuing_bodies'
    issuing_body_id = db.Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False, unique=True)
    # backref from Dispatch