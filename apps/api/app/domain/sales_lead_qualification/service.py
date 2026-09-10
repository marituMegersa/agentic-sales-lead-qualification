from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.sales_lead_qualification.models import AgenticSalesLeadQualificationSession, AgenticSalesLeadQualificationItem
from app.domain.sales_lead_qualification.schemas import AgenticSalesLeadQualificationSessionCreate, AgenticSalesLeadQualificationItemCreate

class AgenticSalesLeadQualificationService:
    @staticmethod
    def create_session(db: Session, data: AgenticSalesLeadQualificationSessionCreate) -> AgenticSalesLeadQualificationSession:
        db_obj = AgenticSalesLeadQualificationSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticSalesLeadQualificationSession:
        return db.query(AgenticSalesLeadQualificationSession).filter(AgenticSalesLeadQualificationSession.id == session_id).first()
