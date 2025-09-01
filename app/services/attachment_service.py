from app import db
from app.models import DispatchAttachment
from datetime import datetime
import uuid


class AttachmentService:
    @staticmethod
    def list_by_dispatch(dispatch_id: str):
        return DispatchAttachment.query.filter_by(dispatch_id=dispatch_id).all()

    @staticmethod
    def create(dispatch_id: str, payload: dict):
        try:
            uuid.UUID(payload["drive_item_id"])
        except ValueError:
            raise ValueError("Invalid UUID format")
        a = DispatchAttachment(
            dispatch_id=dispatch_id,
            drive_item_id=payload["drive_item_id"],
            attached_at=datetime.fromisoformat(payload["attached_at"])
        )
        db.session.add(a)
        db.session.commit()
        return a

    @staticmethod
    def delete(dispatch_id: str, drive_item_id: str):
        a = DispatchAttachment.query.get((dispatch_id, drive_item_id))
        if not a:
            return None
        db.session.delete(a)
        db.session.commit()
        return a
