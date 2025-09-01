# app/controllers/comment_controller.py
from flask import jsonify, request, abort
from app.schemas import DispatchCommentSchema
from app.services import CommentService, DispatchService

comment_schema = DispatchCommentSchema()
comments_schema = DispatchCommentSchema(many=True)


def list_comments(dispatch_id):
    if not DispatchService.get_by_id(dispatch_id):
        abort(404, "Dispatch not found")
    qs = CommentService.list_by_dispatch(dispatch_id)
    return jsonify(comments_schema.dump(qs)), 200


def create_comment(dispatch_id):
    if not DispatchService.get_by_id(dispatch_id):
        abort(404, "Dispatch not found")
    payload = request.get_json() or {}
    errors = comment_schema.validate(payload)
    if errors:
        return jsonify({"errors": errors}), 400
    c = CommentService.create(dispatch_id, payload)
    return jsonify(comment_schema.dump(c)), 201


def update_comment(comment_id):
    c = CommentService.get_by_id(comment_id)
    if not c:
        abort(404, "Comment not found")
    payload = request.get_json() or {}
    errors = comment_schema.validate(payload, partial=True)
    if errors:
        return jsonify({"errors": errors}), 400
    c = CommentService.update(c, payload)
    return jsonify(comment_schema.dump(c)), 200


def delete_comment(comment_id):
    c = CommentService.get_by_id(comment_id)
    if not c:
        abort(404, "Comment not found")
    CommentService.delete(c)
    return '', 204
