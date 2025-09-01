# app/controllers/issuing_body_controller.py
from flask import jsonify, request, abort
from app.schemas import IssuingBodySchema
from app.services import IssuingBodyService

issuing_body_schema = IssuingBodySchema()
issuing_bodies_schema = IssuingBodySchema(many=True)


def list_issuing_bodies():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    qs = IssuingBodyService.get_all(page, per_page)
    return jsonify({
        "items": issuing_bodies_schema.dump(qs.items),
        "total": qs.total,
        "pages": qs.pages,
        "page": page
    }), 200


def get_issuing_body(issuing_body_id):
    ib = IssuingBodyService.get_by_id(issuing_body_id)
    if not ib:
        abort(404, "Issuing body not found")
    return jsonify(issuing_body_schema.dump(ib)), 200


def create_issuing_body():
    payload = request.get_json() or {}
    errors = issuing_body_schema.validate(payload)
    if errors:
        return jsonify({"errors": errors}), 400
    ib = IssuingBodyService.create(payload)
    return jsonify(issuing_body_schema.dump(ib)), 201


def update_issuing_body(issuing_body_id):
    ib = IssuingBodyService.get_by_id(issuing_body_id)
    if not ib:
        abort(404, "Issuing body not found")
    payload = request.get_json() or {}
    errors = issuing_body_schema.validate(payload, partial=True)
    if errors:
        return jsonify({"errors": errors}), 400
    ib = IssuingBodyService.update(ib, payload)
    return jsonify(issuing_body_schema.dump(ib)), 200


def delete_issuing_body(issuing_body_id):
    ib = IssuingBodyService.get_by_id(issuing_body_id)
    if not ib:
        abort(404, "Issuing body not found")
    IssuingBodyService.delete(ib)
    return '', 204
