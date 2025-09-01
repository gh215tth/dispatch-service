# app/controllers/attachment_controller.py
from flask import jsonify, request, abort
from app.schemas import DispatchAttachmentSchema
from app.services import AttachmentService, DispatchService

attachment_schema = DispatchAttachmentSchema()
attachments_schema = DispatchAttachmentSchema(many=True)


def list_attachments(dispatch_id):
    if not DispatchService.get_by_id(dispatch_id):
        abort(404, "Dispatch not found")
    qs = AttachmentService.list_by_dispatch(dispatch_id)
    return jsonify(attachments_schema.dump(qs)), 200


def create_attachment(dispatch_id):
    if not DispatchService.get_by_id(dispatch_id):
        abort(404, "Dispatch not found")
    payload = request.get_json() or {}
    errors = attachment_schema.validate(payload)
    if errors:
        return jsonify({"errors": errors}), 400
    a = AttachmentService.create(dispatch_id, payload)
    return jsonify(attachment_schema.dump(a)), 201


def delete_attachment(dispatch_id, drive_item_id):
    success = AttachmentService.delete(dispatch_id, drive_item_id)
    if not success:
        abort(404, "Attachment not found")
    return '', 204
