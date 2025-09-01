# app/utils/error_handlers.py
from flask import jsonify
from werkzeug.exceptions import HTTPException
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        response = e.get_response()
        response.data = jsonify({
            "error": e.name,
            "description": e.description
        }).data
        response.content_type = "application/json"
        return response, e.code

    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return jsonify({"errors": e.messages}), 400

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(e):
        # rollback should be done in service/controller when catching
        return jsonify({"error": "database_integrity_error", "detail": str(e.orig)}), 400

    @app.errorhandler(Exception)
    def handle_unexpected_error(e):
        # fallback generic handler — in production don't leak stack
        app.logger.exception(e)
        return jsonify({"error": "internal_server_error", "detail": str(e)}), 500
