from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.sales_lead_qualification.schemas import AgenticSalesLeadQualificationSessionCreate, AgenticSalesLeadQualificationSessionResponse
from app.domain.sales_lead_qualification.service import AgenticSalesLeadQualificationService

router = APIRouter(prefix="/api/v1/sales_lead_qualification", tags=["Agentic Sales Lead Qualification Domain"])

@router.post("/sessions", response_model=AgenticSalesLeadQualificationSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticSalesLeadQualificationSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Sales Lead Qualification.
    """
    return AgenticSalesLeadQualificationService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticSalesLeadQualificationSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticSalesLeadQualificationService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
