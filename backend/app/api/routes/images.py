import os
import shutil
import uuid
from pathlib import Path
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.api.routes.projects import get_current_user
from app.models.user import User
from app.models.project import Project
from app.core.config import settings

router = APIRouter()

# Ensure storage directories exist
UPLOAD_DIR = Path(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "storage", "uploads"))
THUMB_DIR = Path(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "storage", "thumbnails"))
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
THUMB_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@router.post("/upload")
def upload_image(
    project_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = db.query(Project).filter(Project.id == project_id, Project.user_id == current_user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="File extension not allowed")

    file_ext = file.filename.rsplit(".", 1)[1].lower()
    unique_filename = f"{uuid.uuid4().hex}.{file_ext}"
    file_path = UPLOAD_DIR / unique_filename

    try:
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {str(e)}")
    
    # Save path to project
    # We store the relative path or absolute path based on architecture, here we store relative to storage
    project.original_image_path = f"uploads/{unique_filename}"
    db.commit()
    db.refresh(project)
    
    return {"message": "Successfully uploaded", "path": project.original_image_path}
