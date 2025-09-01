from app import db
from app.models import DispatchView
from datetime import datetime
import uuid


class ViewService:
    @staticmethod
    def list_by_dispatch(dispatch_id: str):
        return DispatchView.query.filter_by(dispatch_id=dispatch_id).all()

    @staticmethod
    def create(dispatch_id: str, payload: dict):
        try:
            uuid.UUID(payload["user_id"])
        except ValueError:
            raise ValueError("Invalid UUID format")
        v = DispatchView(
            dispatch_id=dispatch_id,
            user_id=payload["user_id"],
            viewed_at=datetime.fromisoformat(payload["viewed_at"])
        )
        db.session.add(v)
        db.session.commit()
        return v

    @staticmethod
    def delete(view_id: str):
        try:
            uid = uuid.UUID(view_id)
        except ValueError:
            raise ValueError("Invalid UUID format")
        v = DispatchView.query.get(uid)
        if not v:
            return None
        db.session.delete(v)
        db.session.commit()
        return v
