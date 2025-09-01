# app/controllers/view_controller.py
from flask import jsonify, request, abort
from app.schemas import DispatchViewSchema
from app.services import ViewService, DispatchService

view_schema = DispatchViewSchema()
views_schema = DispatchViewSchema(many=True)


def list_views(dispatch_id):
    if not DispatchService.get_by_id(dispatch_id):
        abort(404, "Dispatch not found")
    qs = ViewService.list_by_dispatch(dispatch_id)
    return jsonify(views_schema.dump(qs))


def create_view(dispatch_id):
    if not DispatchService.get_by_id(dispatch_id):
        abort(404, "Dispatch not found")
    payload = request.get_json() or {}
    errors = view_schema.validate(payload)
    if errors:
        return jsonify({"errors": errors}), 400
    v = ViewService.create(dispatch_id, payload)
    return jsonify(view_schema.dump(v)), 201


def delete_view(view_id):
    v = ViewService.delete(view_id)
    if not v:
        abort(404, "View not found")
    return jsonify({"message": "deleted"})
