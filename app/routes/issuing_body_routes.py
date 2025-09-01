# app/routes/issuing_body_routes.py
from flask import Blueprint
from app.controllers.issuing_body_controller import (
    list_issuing_bodies, get_issuing_body, create_issuing_body,
    update_issuing_body, delete_issuing_body
)

issuing_body_bp = Blueprint("issuing_bodies", __name__, url_prefix="/api/issuing_bodies")

issuing_body_bp.add_url_rule('/', 'list', list_issuing_bodies, methods=['GET'])
issuing_body_bp.add_url_rule('/<uuid:issuing_body_id>', 'get', get_issuing_body, methods=['GET'])
issuing_body_bp.add_url_rule('/', 'create', create_issuing_body, methods=['POST'])
issuing_body_bp.add_url_rule('/<uuid:issuing_body_id>', 'update', update_issuing_body, methods=['PUT', 'PATCH'])
issuing_body_bp.add_url_rule('/<uuid:issuing_body_id>', 'delete', delete_issuing_body, methods=['DELETE'])
