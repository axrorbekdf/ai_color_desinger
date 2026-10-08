from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(255), index=True)
    
    original_image_path = Column(String(1024), nullable=True)
    modified_image_path = Column(String(1024), nullable=True)
    selected_object_id = Column(Integer, nullable=True)
    
    design_style = Column(String(100), nullable=True)
    mood_goal = Column(String(100), nullable=True)
    
    analysis_data = Column(JSON, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User")
