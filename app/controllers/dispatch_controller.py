# app/controllers/dispatch_controller.py
from flask import jsonify, request, abort
from app.schemas import DispatchSchema
from app.services.dispatch_service import DispatchService

dispatch_schema = DispatchSchema()
dispatches_schema = DispatchSchema(many=True)


def list_dispatches():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    qs = DispatchService.get_all(page, per_page)
    return jsonify({
        "items": dispatches_schema.dump(qs.items),
        "total": qs.total,
        "pages": qs.pages,
        "page": page
    }), 200


def get_dispatch(dispatch_id):
    try:
        d = DispatchService.get_by_id(dispatch_id)
    except ValueError as e:
        abort(400, str(e))
    if not d:
        abort(404, "Dispatch not found")
    return jsonify(dispatch_schema.dump(d)), 200


def create_dispatch():
    payload = request.get_json() or {}
    errors = dispatch_schema.validate(payload)
    if errors:
        return jsonify({"errors": errors}), 400
    try:
        d = DispatchService.create(payload)
        return jsonify(dispatch_schema.dump(d)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


def update_dispatch(dispatch_id):
    try:
        d = DispatchService.get_by_id(dispatch_id)
    except ValueError as e:
        abort(400, str(e))
    if not d:
        abort(404, "Dispatch not found")
    payload = request.get_json() or {}
    errors = dispatch_schema.validate(payload, partial=True)
    if errors:
        return jsonify({"errors": errors}), 400
    d = DispatchService.update(d, payload)
    return jsonify(dispatch_schema.dump(d)), 200


def delete_dispatch(dispatch_id):
    try:
        d = DispatchService.get_by_id(dispatch_id)
    except ValueError as e:
        abort(400, str(e))
    if not d:
        abort(404, "Dispatch not found")
    DispatchService.delete(d)
    return '', 204
