# app/schemas/dispatch_processor_schema.py
from marshmallow import Schema, fields

class DispatchProcessorSchema(Schema):
    dispatch_id = fields.UUID(required=True)
    user_id = fields.UUID(required=True)
    assigned_at = fields.DateTime(required=True)
    deadline = fields.DateTime(allow_none=True)
