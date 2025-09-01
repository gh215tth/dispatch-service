# app/controllers/recipient_controller.py
from flask import jsonify, request, abort
from app.schemas import DispatchRecipientSchema
from app.services import RecipientService, DispatchService

recipient_schema = DispatchRecipientSchema()
recipients_schema = DispatchRecipientSchema(many=True)


def list_recipients(dispatch_id):
    if not DispatchService.get_by_id(dispatch_id):
        abort(404, "Dispatch not found")
    qs = RecipientService.list_by_dispatch(dispatch_id)
    return jsonify(recipients_schema.dump(qs))


def create_recipient(dispatch_id):
    if not DispatchService.get_by_id(dispatch_id):
        abort(404, "Dispatch not found")
    payload = request.get_json() or {}
    errors = recipient_schema.validate(payload)
    if errors:
        return jsonify({"errors": errors}), 400
    r = RecipientService.create(dispatch_id, payload)
    return jsonify(recipient_schema.dump(r)), 201


def delete_recipient(dispatch_id, user_id):
    r = RecipientService.delete(dispatch_id, user_id)
    if not r:
        abort(404, "Recipient not found")
    return jsonify({"message": "deleted"})
