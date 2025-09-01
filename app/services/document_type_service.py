from app import db
from app.models import DocumentType
import uuid


class DocumentTypeService:
    @staticmethod
    def get_all(page=1, per_page=10):
        return DocumentType.query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def get_by_id(document_type_id: str):
        try:
            uid = uuid.UUID(document_type_id)
        except ValueError:
            raise ValueError("Invalid UUID format")
        return DocumentType.query.get(uid)

    @staticmethod
    def create(payload: dict):
        dt = DocumentType(
            name=payload["name"],
            description=payload.get("description")
        )
        db.session.add(dt)
        db.session.commit()
        return dt

    @staticmethod
    def update(dt: DocumentType, payload: dict):
        for k, v in payload.items():
            if hasattr(dt, k):
                setattr(dt, k, v)
        db.session.commit()
        return dt

    @staticmethod
    def delete(dt: DocumentType):
        db.session.delete(dt)
        db.session.commit()
