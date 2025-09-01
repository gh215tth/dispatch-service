# models/document_type.py
from app import db
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
import uuid

class DocumentType(db.Model):
    __tablename__ = 'document_types'
    document_type_id = db.Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.Text)
    # backref from Dispatch