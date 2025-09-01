from app import db
from app.models import DispatchProcessor
from datetime import datetime
import uuid


class ProcessorService:
    @staticmethod
    def list_by_dispatch(dispatch_id: str):
        return DispatchProcessor.query.filter_by(dispatch_id=dispatch_id).all()

    @staticmethod
    def create(dispatch_id: str, payload: dict):
        try:
            uuid.UUID(payload["user_id"])
        except ValueError:
            raise ValueError("Invalid UUID format")
        p = DispatchProcessor(
            dispatch_id=dispatch_id,
            user_id=payload["user_id"],
            assigned_at=datetime.fromisoformat(payload["assigned_at"]),
            deadline=datetime.fromisoformat(payload["deadline"]) if payload.get("deadline") else None
        )
        db.session.add(p)
        db.session.commit()
        return p

    @staticmethod
    def delete(dispatch_id: str, user_id: str):
        p = DispatchProcessor.query.get((dispatch_id, user_id))
        if not p:
            return None
        db.session.delete(p)
        db.session.commit()
        return p
