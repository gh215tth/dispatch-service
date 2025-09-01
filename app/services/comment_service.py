from app import db
from app.models import DispatchComment
from datetime import datetime
import uuid


class CommentService:
    @staticmethod
    def list_by_dispatch(dispatch_id: str):
        return DispatchComment.query.filter_by(dispatch_id=dispatch_id).order_by(DispatchComment.created_at.desc()).all()

    @staticmethod
    def create(dispatch_id: str, payload: dict):
        try:
            uuid.UUID(payload["author_user_id"])
        except ValueError:
            raise ValueError("Invalid UUID format")
        c = DispatchComment(
            dispatch_id=dispatch_id,
            author_user_id=payload["author_user_id"],
            content=payload["content"],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(c)
        db.session.commit()
        return c

    @staticmethod
    def update(c: DispatchComment, payload: dict):
        for k, v in payload.items():
            if hasattr(c, k):
                setattr(c, k, v)
        c.updated_at = datetime.utcnow()
        db.session.commit()
        return c

    @staticmethod
    def delete(c: DispatchComment):
        db.session.delete(c)
        db.session.commit()

    @staticmethod
    def get_by_id(comment_id: str):
        try:
            uid = uuid.UUID(comment_id)
        except ValueError:
            raise ValueError("Invalid UUID format")
        return DispatchComment.query.get(uid)

