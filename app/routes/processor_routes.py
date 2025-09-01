# app/routes/processor_routes.py
from flask import Blueprint
from app.controllers.processor_controller import (
    list_processors, create_processor, delete_processor
)

processor_bp = Blueprint("processors", __name__, url_prefix="/api/dispatches/<uuid:dispatch_id>/processors")

processor_bp.add_url_rule('/', 'list', list_processors, methods=['GET'])
processor_bp.add_url_rule('/', 'create', create_processor, methods=['POST'])
processor_bp.add_url_rule('/<uuid:user_id>', 'delete', delete_processor, methods=['DELETE'])
