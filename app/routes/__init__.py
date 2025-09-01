# app/routes/__init__.py
from .dispatch_routes import dispatch_bp
from .document_type_routes import document_type_bp
from .issuing_body_routes import issuing_body_bp
from .attachment_routes import attachment_bp
from .comment_routes import comment_bp
from .recipient_routes import recipient_bp
from .processor_routes import processor_bp
from .follower_routes import follower_bp
from .view_routes import view_bp

def register_routes(app):
    app.register_blueprint(dispatch_bp)
    app.register_blueprint(document_type_bp)
    app.register_blueprint(issuing_body_bp)
    app.register_blueprint(attachment_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(recipient_bp)
    app.register_blueprint(processor_bp)
    app.register_blueprint(follower_bp)
    app.register_blueprint(view_bp)
