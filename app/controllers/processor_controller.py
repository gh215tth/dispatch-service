# app/controllers/processor_controller.py
from flask import jsonify, request, abort
from app.schemas import DispatchProcessorSchema
from app.services import ProcessorService, DispatchService

processor_schema = DispatchProcessorSchema()
processors_schema = DispatchProcessorSchema(many=True)


def list_processors(dispatch_id):
    if not DispatchService.get_by_id(dispatch_id):
        abort(404, "Dispatch not found")
    qs = ProcessorService.list_by_dispatch(dispatch_id)
    return jsonify(processors_schema.dump(qs))


def create_processor(dispatch_id):
    if not DispatchService.get_by_id(dispatch_id):
        abort(404, "Dispatch not found")
    payload = request.get_json() or {}
    errors = processor_schema.validate(payload)
    if errors:
        return jsonify({"errors": errors}), 400
    p = ProcessorService.create(dispatch_id, payload)
    return jsonify(processor_schema.dump(p)), 201


def delete_processor(dispatch_id, user_id):
    p = ProcessorService.delete(dispatch_id, user_id)
    if not p:
        abort(404, "Processor not found")
    return jsonify({"message": "deleted"})
