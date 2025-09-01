# app/schemas/dispatch_view_schema.py
from marshmallow import Schema, fields

class DispatchViewSchema(Schema):
    view_id = fields.UUID(dump_only=True)
    dispatch_id = fields.UUID(required=True)
    user_id = fields.UUID(required=True)
    viewed_at = fields.DateTime(required=True)
