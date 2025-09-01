# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Khởi tạo DB và migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Đăng ký error handlers
    from app.units.error_handlers import register_error_handlers
    register_error_handlers(app)

    # Import models để Flask-Migrate nhận diện
    from app import models

    # Import và đăng ký routes
    from app.routes import (
        dispatch_bp,
        attachment_bp,
        comment_bp,
        document_type_bp,
        follower_bp,
        issuing_body_bp,
        processor_bp,
        recipient_bp,
        view_bp,
    )

    app.register_blueprint(dispatch_bp)
    app.register_blueprint(attachment_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(document_type_bp)
    app.register_blueprint(follower_bp)
    app.register_blueprint(issuing_body_bp)
    app.register_blueprint(processor_bp)
    app.register_blueprint(recipient_bp)
    app.register_blueprint(view_bp)

    return app
