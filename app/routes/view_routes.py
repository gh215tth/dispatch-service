# app/routes/view_routes.py
from flask import Blueprint
from app.controllers.view_controller import (
    list_views, create_view, delete_view
)

view_bp = Blueprint("views", __name__)

# list/create under dispatch
view_bp.add_url_rule('/api/dispatches/<uuid:dispatch_id>/views', 'list_views', list_views, methods=['GET'])
view_bp.add_url_rule('/api/dispatches/<uuid:dispatch_id>/views', 'create_view', create_view, methods=['POST'])

# delete a view by its id
view_bp.add_url_rule('/api/views/<uuid:view_id>', 'delete_view', delete_view, methods=['DELETE'])
