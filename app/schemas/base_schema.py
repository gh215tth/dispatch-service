# app/schemas/base_schema.py
from marshmallow import Schema, fields, validate

UUIDField = fields.UUID
StringField = lambda **kwargs: fields.Str(validate=validate.Length(min=1, **(kwargs or {})))
DateTimeField = fields.DateTime
IntField = fields.Int
