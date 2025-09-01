# app/services/dispatch_service.py
from app import db
from app.models import Dispatch, DocumentType, IssuingBody
from datetime import datetime
import uuid


class DispatchService:
    @staticmethod
    def get_all(page=1, per_page=10):
        return Dispatch.query.order_by(Dispatch.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )

    @staticmethod
    def get_by_id(dispatch_id: str):
        try:
            uid = uuid.UUID(dispatch_id)
        except ValueError:
            raise ValueError("Invalid UUID format")
        return Dispatch.query.get(uid)

    @staticmethod
    def create(payload: dict):
        if not DocumentType.query.get(payload["document_type_id"]):
            raise ValueError("document_type_id not found")
        if not IssuingBody.query.get(payload["issuing_body_id"]):
            raise ValueError("issuing_body_id not found")

        d = Dispatch(
            document_number=payload["document_number"],
            summary=payload.get("summary"),
            page_count=payload.get("page_count"),
            security_level=payload["security_level"],
            urgency_level=payload["urgency_level"],
            processing_status=payload["processing_status"],
            document_type_id=payload["document_type_id"],
            issuing_body_id=payload["issuing_body_id"],
            creator_user_id=payload["creator_user_id"],
            approver_user_id=payload.get("approver_user_id"),
            arrival_timestamp=DispatchService._parse_date(payload.get("arrival_timestamp")),
            effective_timestamp=DispatchService._parse_date(payload.get("effective_timestamp")),
            expiration_timestamp=DispatchService._parse_date(payload.get("expiration_timestamp")),
            approved_at=DispatchService._parse_date(payload.get("approved_at")),
        )
        db.session.add(d)
        db.session.commit()
        return d

    @staticmethod
    def update(d: Dispatch, payload: dict):
        for k, v in payload.items():
            if k in ["arrival_timestamp", "effective_timestamp", "expiration_timestamp", "approved_at"] and v:
                v = DispatchService._parse_date(v)
            if hasattr(d, k):
                setattr(d, k, v)
        d.updated_at = datetime.utcnow()
        db.session.commit()
        return d

    @staticmethod
    def delete(d: Dispatch):
        db.session.delete(d)
        db.session.commit()

    @staticmethod
    def _parse_date(value: str):
        if value:
            return datetime.fromisoformat(value)
        return None
