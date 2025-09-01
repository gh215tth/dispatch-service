from app import db
from app.models import DispatchRecipient
from datetime import datetime
import uuid


class RecipientService:
    @staticmethod
    def list_by_dispatch(dispatch_id: str):
        return DispatchRecipient.query.filter_by(dispatch_id=dispatch_id).all()

    @staticmethod
    def create(dispatch_id: str, payload: dict):
        try:
            uuid.UUID(payload["user_id"])
        except ValueError:
            raise ValueError("Invalid UUID format")
        r = DispatchRecipient(
            dispatch_id=dispatch_id,
            user_id=payload["user_id"],
            notified_at=datetime.fromisoformat(payload["notified_at"]) if payload.get("notified_at") else None
        )
        db.session.add(r)
        db.session.commit()
        return r

    @staticmethod
    def delete(dispatch_id: str, user_id: str):
        r = DispatchRecipient.query.get((dispatch_id, user_id))
        if not r:
            return None
        db.session.delete(r)
        db.session.commit()
        return r
