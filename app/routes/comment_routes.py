# app/routes/comment_routes.py
from flask import Blueprint
from app.controllers.comment_controller import (
    list_comments, create_comment, update_comment, delete_comment
)

# list/create nested under dispatch
comment_bp = Blueprint("comments", __name__)

# list & create for comments under a dispatch
comment_bp.add_url_rule('/api/dispatches/<uuid:dispatch_id>/comments', 'list_comments', list_comments, methods=['GET'])
comment_bp.add_url_rule('/api/dispatches/<uuid:dispatch_id>/comments', 'create_comment', create_comment, methods=['POST'])

# update & delete by comment id
comment_bp.add_url_rule('/api/comments/<uuid:comment_id>', 'update_comment', update_comment, methods=['PUT', 'PATCH'])
comment_bp.add_url_rule('/api/comments/<uuid:comment_id>', 'delete_comment', delete_comment, methods=['DELETE'])
