from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List, Optional

from app.api.dependencies import get_db
from app.api.routes.projects import get_current_user
from app.models.user import User
from app.models.project import Project
from app.models.analysis import DetectedObject, ColorRecommendation
from app.services.color import get_dominant_colors
from app.services.recommendation import generate_recommendations

import os
from pathlib import Path

router = APIRouter()

class ColorRecommendRequest(BaseModel):
    object_id: int

@router.post("/recommend/{project_id}")
def recommend_colors(project_id: int, request: ColorRecommendRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = db.query(Project).filter(Project.id == project_id, Project.user_id == current_user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    detected_obj = db.query(DetectedObject).filter(
        DetectedObject.id == request.object_id,
        DetectedObject.project_id == project.id
    ).first()
    
    if not detected_obj:
        raise HTTPException(status_code=404, detail="Object not found")

    storage_root = Path(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "storage"))
    img_path = storage_root.parent / "storage" / project.original_image_path
    
    # 1. Color extraction (Masked object)
    if detected_obj.segmentation_mask_path:
        mask_path = storage_root.parent / "storage" / detected_obj.segmentation_mask_path
        obj_colors = get_dominant_colors(str(img_path), str(mask_path), n_colors=1)
        if obj_colors:
            detected_obj.original_color = obj_colors[0]
            
    # 2. Extract environment colors
    env_colors = get_dominant_colors(str(img_path), n_colors=5)
    
    # 3. Generate recommendations
    recs = generate_recommendations(
        env_colors=env_colors,
        design_style=project.design_style or "Modern",
        mood_goal=project.mood_goal or "Calm",
        n_recommendations=5
    )
    
    # 4. Save recommendations to DB
    saved_recs = []
    for rec in recs:
        db_rec = ColorRecommendation(
            project_id=project.id,
            object_id=detected_obj.id,
            color_name=rec["color_name"],
            hex_val=rec["hex_val"],
            rgb_val=rec["rgb_val"],
            hsv_val=rec["hsv_val"],
            compatibility_score=rec["compatibility_score"],
            harmony_score=rec["harmony_score"],
            mood_score=rec["mood_score"],
            recommendation_reason=rec["recommendation_reason"]
        )
        db.add(db_rec)
        saved_recs.append(db_rec)
        
    db.commit()
    for r in saved_recs:
        db.refresh(r)
        
    return {"message": "Recommendations generated", "recommendations": saved_recs}
