# app/routes/dispatch_routes.py
from flask import Blueprint
from app.controllers.dispatch_controller import (
    list_dispatches, get_dispatch, create_dispatch, update_dispatch, delete_dispatch
)

dispatch_bp = Blueprint("dispatch", __name__, url_prefix="/api/dispatches")

dispatch_bp.add_url_rule('/', 'list', list_dispatches, methods=['GET'])
dispatch_bp.add_url_rule('/<uuid:dispatch_id>', 'get', get_dispatch, methods=['GET'])
dispatch_bp.add_url_rule('/', 'create', create_dispatch, methods=['POST'])
dispatch_bp.add_url_rule('/<uuid:dispatch_id>', 'update', update_dispatch, methods=['PUT','PATCH'])
dispatch_bp.add_url_rule('/<uuid:dispatch_id>', 'delete', delete_dispatch, methods=['DELETE'])
