# app/routes/attachment_routes.py
from flask import Blueprint
from app.controllers.attachment_controller import (
    list_attachments, create_attachment, delete_attachment
)

attachment_bp = Blueprint("attachments", __name__, url_prefix="/api/dispatches/<uuid:dispatch_id>/attachments")

attachment_bp.add_url_rule('/', 'list', list_attachments, methods=['GET'])
attachment_bp.add_url_rule('/', 'create', create_attachment, methods=['POST'])
attachment_bp.add_url_rule('/<uuid:drive_item_id>', 'delete', delete_attachment, methods=['DELETE'])
