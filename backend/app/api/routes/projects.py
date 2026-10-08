from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from app.models.project import Project
from app.models.user import User
from app.core.config import settings
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return user

@router.post("/", response_model=ProjectResponse)
def create_project(project_in: ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = Project(
        name=project_in.name,
        user_id=current_user.id,
        design_style=project_in.design_style,
        mood_goal=project_in.mood_goal
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

@router.get("/", response_model=List[ProjectResponse])
def get_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    projects = db.query(Project).filter(Project.user_id == current_user.id).order_by(Project.created_at.desc()).offset(skip).limit(limit).all()
    return projects

@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = db.query(Project).filter(Project.id == project_id, Project.user_id == current_user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = db.query(Project).filter(Project.id == project_id, Project.user_id == current_user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    # Manually cascade delete to avoid FK constraints
    from app.models.analysis import ColorRecommendation, DetectedObject
    from app.models.project import ProjectResult
    
    db.query(ColorRecommendation).filter(ColorRecommendation.project_id == project_id).delete()
    db.query(DetectedObject).filter(DetectedObject.project_id == project_id).delete()
    db.query(ProjectResult).filter(ProjectResult.project_id == project_id).delete()
    
    db.delete(project)
    db.commit()
    return {"message": "Project deleted successfully"}

@router.get("/user/results")
def get_user_results(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    from app.models.project import ProjectResult
    
    # Get all results for projects owned by this user
    results = db.query(ProjectResult).join(Project).filter(Project.user_id == current_user.id).order_by(ProjectResult.created_at.desc()).all()
    
    return [
        {
            "id": r.id,
            "project_id": r.project_id,
            "project_name": r.project.name if r.project else f"Loyiha {r.project_id}",
            "name": r.name,
            "result_image_path": r.result_image_path,
            "action_description": r.action_description,
            "created_at": r.created_at
        } for r in results
    ]
