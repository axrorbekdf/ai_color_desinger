import os
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.api.routes.projects import get_current_user
from app.models.user import User
from app.models.project import Project
from app.models.analysis import DetectedObject
from app.services.segmentation import get_segmentation_model
from app.core.config import settings
from pathlib import Path
import cv2

router = APIRouter()
MASKS_DIR = Path(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "storage", "masks"))
MASKS_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/segment/{project_id}")
def segment_image(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = db.query(Project).filter(Project.id == project_id, Project.user_id == current_user.id).first()
    if not project or not project.original_image_path:
        raise HTTPException(status_code=404, detail="Project or image not found")

    # Absolute path to the image
    storage_root = Path(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "storage"))
    img_path = storage_root.parent / "storage" / project.original_image_path
    
    if not img_path.exists():
        raise HTTPException(status_code=404, detail="Image file missing on disk")

    model = get_segmentation_model()
    try:
        predictions = model.predict(str(img_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Segmentation failed: {str(e)}")

    objects_created = []
    
    for i, pred in enumerate(predictions):
        # Save mask as an image
        mask_filename = f"{uuid.uuid4().hex}_mask.png"
        mask_path = MASKS_DIR / mask_filename
        cv2.imwrite(str(mask_path), pred["mask"])
        
        db_obj = DetectedObject(
            project_id=project.id,
            object_type=pred["object_type"],
            confidence=pred["confidence"],
            bounding_box=pred["bounding_box"],
            segmentation_mask_path=f"masks/{mask_filename}"
        )
        db.add(db_obj)
        objects_created.append(db_obj)
        
    db.commit()
    for obj in objects_created:
        db.refresh(obj)
        
    return {"message": f"Found {len(objects_created)} objects", "objects": objects_created}
