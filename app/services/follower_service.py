from app import db
from app.models import DispatchFollower
from datetime import datetime
import uuid


class FollowerService:
    @staticmethod
    def list_by_dispatch(dispatch_id: str):
        return DispatchFollower.query.filter_by(dispatch_id=dispatch_id).all()

    @staticmethod
    def create(dispatch_id: str, payload: dict):
        try:
            uuid.UUID(payload["user_id"])
        except ValueError:
            raise ValueError("Invalid UUID format")
        f = DispatchFollower(
            dispatch_id=dispatch_id,
            user_id=payload["user_id"],
            followed_at=datetime.fromisoformat(payload["followed_at"])
        )
        db.session.add(f)
        db.session.commit()
        return f

    @staticmethod
    def delete(dispatch_id: str, user_id: str):
        f = DispatchFollower.query.get((dispatch_id, user_id))
        if not f:
            return None
        db.session.delete(f)
        db.session.commit()
        return f
