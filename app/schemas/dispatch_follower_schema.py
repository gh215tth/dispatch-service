# app/schemas/dispatch_follower_schema.py
from marshmallow import Schema, fields

class DispatchFollowerSchema(Schema):
    dispatch_id = fields.UUID(required=True)
    user_id = fields.UUID(required=True)
    followed_at = fields.DateTime(required=True)
