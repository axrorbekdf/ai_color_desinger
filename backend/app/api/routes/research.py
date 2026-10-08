from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from app.api.dependencies import get_db
from app.api.routes.projects import get_current_user
from app.models.user import User
from app.models.feedback import UserFeedback, MLExperiment
from app.services.ml_pipeline import train_and_evaluate_ml_model

router = APIRouter()

class FeedbackCreate(BaseModel):
    project_id: int
    recommendation_id: int
    rating: int
    accepted: bool
    comment: str = None

@router.post("/feedback")
def submit_feedback(feedback_in: FeedbackCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    fb = UserFeedback(
        project_id=feedback_in.project_id,
        recommendation_id=feedback_in.recommendation_id,
        rating=feedback_in.rating,
        accepted=feedback_in.accepted,
        comment=feedback_in.comment
    )
    db.add(fb)
    db.commit()
    db.refresh(fb)
    return {"message": "Feedback saved successfully"}

@router.get("/statistics")
def get_research_statistics(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Simple aggregates
    total_feedbacks = db.query(UserFeedback).count()
    accepted = db.query(UserFeedback).filter(UserFeedback.accepted == True).count()
    avg_rating = db.query(func.avg(UserFeedback.rating)).scalar() or 0.0
    
    acceptance_rate = (accepted / total_feedbacks * 100) if total_feedbacks > 0 else 0
    
    return {
        "total_feedbacks": total_feedbacks,
        "acceptance_rate": round(acceptance_rate, 2),
        "avg_rating": round(avg_rating, 2)
    }

class MLTrainRequest(BaseModel):
    model_type: str

@router.post("/ml/train")
def train_ml_model(request: MLTrainRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = train_and_evaluate_ml_model(db, request.model_type)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.get("/ml/experiments")
def get_ml_experiments(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    experiments = db.query(MLExperiment).order_by(MLExperiment.created_at.desc()).all()
    return experiments
