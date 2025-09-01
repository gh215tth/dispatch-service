# app/controllers/follower_controller.py
from flask import jsonify, request, abort
from app.schemas import DispatchFollowerSchema
from app.services import FollowerService, DispatchService

follower_schema = DispatchFollowerSchema()
followers_schema = DispatchFollowerSchema(many=True)


def list_followers(dispatch_id):
    if not DispatchService.get_by_id(dispatch_id):
        abort(404, "Dispatch not found")
    qs = FollowerService.list_by_dispatch(dispatch_id)
    return jsonify(followers_schema.dump(qs))


def create_follower(dispatch_id):
    if not DispatchService.get_by_id(dispatch_id):
        abort(404, "Dispatch not found")
    payload = request.get_json() or {}
    errors = follower_schema.validate(payload)
    if errors:
        return jsonify({"errors": errors}), 400
    f = FollowerService.create(dispatch_id, payload)
    return jsonify(follower_schema.dump(f)), 201


def delete_follower(dispatch_id, user_id):
    f = FollowerService.delete(dispatch_id, user_id)
    if not f:
        abort(404, "Follower not found")
    return jsonify({"message": "deleted"})
