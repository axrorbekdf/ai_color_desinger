import os
import uuid
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.api.routes.projects import get_current_user
from app.models.user import User
from app.models.project import Project
from app.models.analysis import DetectedObject, ColorRecommendation
from app.services.recolor import recolor_object
from app.core.config import settings

router = APIRouter()
PROCESSED_DIR = Path(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "storage", "processed"))
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

class RecolorRequest(BaseModel):
    recommendation_id: int

@router.post("/{project_id}")
def apply_recolor(project_id: int, request: RecolorRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = db.query(Project).filter(Project.id == project_id, Project.user_id == current_user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    rec = db.query(ColorRecommendation).filter(ColorRecommendation.id == request.recommendation_id, ColorRecommendation.project_id == project.id).first()
    if not rec:
        raise HTTPException(status_code=404, detail="Recommendation not found")
        
    obj = rec.detected_object
    if not obj or not obj.segmentation_mask_path:
        raise HTTPException(status_code=400, detail="Object or mask not found")

    storage_root = Path(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "storage"))
    
    # Allow cumulative recoloring by using the modified image as the base if it exists
    base_image = project.modified_image_path if project.modified_image_path else project.original_image_path
    img_path = storage_root.parent / "storage" / base_image
    
    mask_path = storage_root.parent / "storage" / obj.segmentation_mask_path
    
    output_filename = f"{uuid.uuid4().hex}_recolored.jpg"
    output_path = PROCESSED_DIR / output_filename
    
    try:
        recolor_object(str(img_path), str(mask_path), rec.hex_val, str(output_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Recoloring failed: {str(e)}")
        
    # Mark recommendation as selected
    rec.selected = True
    
    # Update project
    project.modified_image_path = f"processed/{output_filename}"
    project.selected_object_id = obj.id
    
    from app.models.project import ProjectResult
    result_record = ProjectResult(
        project_id=project.id,
        name=f"Loyiha {project.id} natijasi",
        result_image_path=project.modified_image_path,
        action_description=f"{obj.object_type} obyekti {rec.hex_val} rangiga bo'yaldi"
    )
    db.add(result_record)
    
    db.commit()
    db.refresh(project)
    
    return {"message": "Recolored successfully", "modified_image_path": project.modified_image_path}

@router.post("/reset/{project_id}")
def reset_recolor(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = db.query(Project).filter(Project.id == project_id, Project.user_id == current_user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    project.modified_image_path = None
    db.commit()
    return {"message": "Reset successful"}
