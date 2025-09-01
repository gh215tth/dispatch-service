# app/routes/recipient_routes.py
from flask import Blueprint
from app.controllers.recipient_controller import (
    list_recipients, create_recipient, delete_recipient
)

recipient_bp = Blueprint("recipients", __name__, url_prefix="/api/dispatches/<uuid:dispatch_id>/recipients")

recipient_bp.add_url_rule('/', 'list', list_recipients, methods=['GET'])
recipient_bp.add_url_rule('/', 'create', create_recipient, methods=['POST'])
recipient_bp.add_url_rule('/<uuid:user_id>', 'delete', delete_recipient, methods=['DELETE'])
