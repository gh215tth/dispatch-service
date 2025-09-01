# app/schemas/dispatch_schema.py
from marshmallow import Schema, fields, validate, post_dump, EXCLUDE
from .document_type_schema import DocumentTypeSchema
from .issuing_body_schema import IssuingBodySchema

class DispatchSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    dispatch_id = fields.UUID(dump_only=True)
    document_number = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    summary = fields.Str(allow_none=True)
    page_count = fields.Int(allow_none=True, validate=validate.Range(min=1))

    # enums must match DB enum values
    security_level = fields.Str(
        required=True,
        validate=validate.OneOf(['public', 'internal', 'confidential'])
    )
    urgency_level = fields.Str(
        required=True,
        validate=validate.OneOf(['normal', 'urgent', 'immediate'])
    )
    processing_status = fields.Str(
        required=True,
        validate=validate.OneOf(['pending', 'in_progress', 'completed', 'archived'])
    )

    document_type_id = fields.UUID(required=True, load_only=True)
    issuing_body_id = fields.UUID(required=True, load_only=True)
    creator_user_id = fields.UUID(required=True)
    approver_user_id = fields.UUID(allow_none=True)

    arrival_timestamp = fields.DateTime(allow_none=True)
    effective_timestamp = fields.DateTime(allow_none=True)
    expiration_timestamp = fields.DateTime(allow_none=True)
    approved_at = fields.DateTime(allow_none=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    # Nested (dump only) for helpful responses
    document_type = fields.Nested(DocumentTypeSchema, dump_only=True)
    issuing_body = fields.Nested(IssuingBodySchema, dump_only=True)

    @post_dump
    def ensure_ids(self, data, **kwargs):
        # Ensure nested document_type/issuing_body don't duplicate IDs in output
        # (Optional tweak: remove nested if not present)
        return data
