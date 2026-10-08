from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class ProjectBase(BaseModel):
    name: str
    design_style: Optional[str] = None
    mood_goal: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    name: Optional[str] = None
    original_image_path: Optional[str] = None
    modified_image_path: Optional[str] = None
    selected_object_id: Optional[int] = None
    analysis_data: Optional[Dict[str, Any]] = None

class ProjectResponse(ProjectBase):
    id: int
    user_id: int
    original_image_path: Optional[str] = None
    modified_image_path: Optional[str] = None
    selected_object_id: Optional[int] = None
    analysis_data: Optional[Dict[str, Any]] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
