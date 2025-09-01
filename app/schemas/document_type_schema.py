# app/schemas/document_type_schema.py
from marshmallow import Schema, fields, validate

class DocumentTypeSchema(Schema):
    document_type_id = fields.UUID(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    description = fields.Str(allow_none=True)
