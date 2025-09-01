# app/schemas/issuing_body_schema.py
from marshmallow import Schema, fields, validate

class IssuingBodySchema(Schema):
    issuing_body_id = fields.UUID(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=255))
