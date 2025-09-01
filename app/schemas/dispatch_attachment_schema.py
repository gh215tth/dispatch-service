# app/schemas/dispatch_attachment_schema.py
from marshmallow import Schema, fields

class DispatchAttachmentSchema(Schema):
    dispatch_id = fields.UUID(required=True)
    drive_item_id = fields.UUID(required=True)
    attached_at = fields.DateTime(required=True)
