from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON, Float, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class DetectedObject(Base):
    __tablename__ = "detected_objects"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    
    object_type = Column(String(255))
    confidence = Column(Float)
    
    bounding_box = Column(JSON)
    segmentation_mask_path = Column(String(1024))
    
    original_color = Column(JSON)
    dominant_colors = Column(JSON)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    project = relationship("Project")

class ColorRecommendation(Base):
    __tablename__ = "color_recommendations"
    
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    object_id = Column(Integer, ForeignKey("detected_objects.id"), nullable=False)
    
    color_name = Column(String(255))
    hex_val = Column(String(10))
    rgb_val = Column(JSON)
    hsv_val = Column(JSON)
    lab_val = Column(JSON)
    
    compatibility_score = Column(Float)
    harmony_score = Column(Float)
    mood_score = Column(Float)
    
    recommendation_reason = Column(String(1024))
    selected = Column(Boolean, default=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    project = relationship("Project")
    detected_object = relationship("DetectedObject")
