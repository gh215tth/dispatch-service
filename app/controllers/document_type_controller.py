# app/controllers/document_type_controller.py
from flask import jsonify, request, abort
from app.schemas import DocumentTypeSchema
from app.services import DocumentTypeService

document_type_schema = DocumentTypeSchema()
document_types_schema = DocumentTypeSchema(many=True)


def list_document_types():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    qs = DocumentTypeService.get_all(page, per_page)
    return jsonify({
        "items": document_types_schema.dump(qs.items),
        "total": qs.total,
        "pages": qs.pages,
        "page": page
    }), 200


def get_document_type(document_type_id):
    dt = DocumentTypeService.get_by_id(document_type_id)
    if not dt:
        abort(404, "Document type not found")
    return jsonify(document_type_schema.dump(dt)), 200


def create_document_type():
    payload = request.get_json() or {}
    errors = document_type_schema.validate(payload)
    if errors:
        return jsonify({"errors": errors}), 400
    dt = DocumentTypeService.create(payload)
    return jsonify(document_type_schema.dump(dt)), 201


def update_document_type(document_type_id):
    dt = DocumentTypeService.get_by_id(document_type_id)
    if not dt:
        abort(404, "Document type not found")
    payload = request.get_json() or {}
    errors = document_type_schema.validate(payload, partial=True)
    if errors:
        return jsonify({"errors": errors}), 400
    dt = DocumentTypeService.update(dt, payload)
    return jsonify(document_type_schema.dump(dt)), 200


def delete_document_type(document_type_id):
    dt = DocumentTypeService.get_by_id(document_type_id)
    if not dt:
        abort(404, "Document type not found")
    DocumentTypeService.delete(dt)
    return '', 204
