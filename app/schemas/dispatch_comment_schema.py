# app/schemas/dispatch_comment_schema.py
from marshmallow import Schema, fields, validate

class DispatchCommentSchema(Schema):
    comment_id = fields.UUID(dump_only=True)
    dispatch_id = fields.UUID(required=True)
    author_user_id = fields.UUID(required=True)
    content = fields.Str(required=True, validate=validate.Length(min=1))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
