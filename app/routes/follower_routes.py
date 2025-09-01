# app/routes/follower_routes.py
from flask import Blueprint
from app.controllers.follower_controller import (
    list_followers, create_follower, delete_follower
)

follower_bp = Blueprint("followers", __name__, url_prefix="/api/dispatches/<uuid:dispatch_id>/followers")

follower_bp.add_url_rule('/', 'list', list_followers, methods=['GET'])
follower_bp.add_url_rule('/', 'create', create_follower, methods=['POST'])
follower_bp.add_url_rule('/<uuid:user_id>', 'delete', delete_follower, methods=['DELETE'])
