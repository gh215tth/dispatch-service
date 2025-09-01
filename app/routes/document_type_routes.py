# app/routes/document_type_routes.py
from flask import Blueprint
from app.controllers.document_type_controller import (
    list_document_types, get_document_type, create_document_type,
    update_document_type, delete_document_type
)

document_type_bp = Blueprint("document_types", __name__, url_prefix="/api/document_types")

document_type_bp.add_url_rule('/', 'list', list_document_types, methods=['GET'])
document_type_bp.add_url_rule('/<uuid:document_type_id>', 'get', get_document_type, methods=['GET'])
document_type_bp.add_url_rule('/', 'create', create_document_type, methods=['POST'])
document_type_bp.add_url_rule('/<uuid:document_type_id>', 'update', update_document_type, methods=['PUT', 'PATCH'])
document_type_bp.add_url_rule('/<uuid:document_type_id>', 'delete', delete_document_type, methods=['DELETE'])
