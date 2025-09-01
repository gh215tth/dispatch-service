# app/schemas/dispatch_recipient_schema.py
from marshmallow import Schema, fields

class DispatchRecipientSchema(Schema):
    dispatch_id = fields.UUID(required=True)
    user_id = fields.UUID(required=True)
    notified_at = fields.DateTime(allow_none=True)
