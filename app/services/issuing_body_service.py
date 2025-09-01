from app import db
from app.models import IssuingBody
import uuid


class IssuingBodyService:
    @staticmethod
    def get_all(page=1, per_page=10):
        return IssuingBody.query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def get_by_id(issuing_body_id: str):
        try:
            uid = uuid.UUID(issuing_body_id)
        except ValueError:
            raise ValueError("Invalid UUID format")
        return IssuingBody.query.get(uid)

    @staticmethod
    def create(payload: dict):
        ib = IssuingBody(name=payload["name"])
        db.session.add(ib)
        db.session.commit()
        return ib

    @staticmethod
    def update(ib: IssuingBody, payload: dict):
        for k, v in payload.items():
            if hasattr(ib, k):
                setattr(ib, k, v)
        db.session.commit()
        return ib

    @staticmethod
    def delete(ib: IssuingBody):
        db.session.delete(ib)
        db.session.commit()
