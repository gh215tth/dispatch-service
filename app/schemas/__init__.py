# app/schemas/__init__.py
from .document_type_schema import DocumentTypeSchema
from .issuing_body_schema import IssuingBodySchema
from .dispatch_recipient_schema import DispatchRecipientSchema
from .dispatch_processor_schema import DispatchProcessorSchema
from .dispatch_follower_schema import DispatchFollowerSchema
from .dispatch_attachment_schema import DispatchAttachmentSchema
from .dispatch_comment_schema import DispatchCommentSchema
from .dispatch_view_schema import DispatchViewSchema
from .dispatch_schema import DispatchSchema

__all__ = [
    "DocumentTypeSchema",
    "IssuingBodySchema",
    "DispatchRecipientSchema",
    "DispatchProcessorSchema",
    "DispatchFollowerSchema",
    "DispatchAttachmentSchema",
    "DispatchCommentSchema",
    "DispatchViewSchema",
    "DispatchSchema",
]
