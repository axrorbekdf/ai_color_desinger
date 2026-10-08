from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class UserFeedback(Base):
    __tablename__ = "user_feedback"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    recommendation_id = Column(Integer, ForeignKey("color_recommendations.id"), nullable=False)
    
    rating = Column(Integer, nullable=False)  # 1 to 5
    accepted = Column(Boolean, default=False)
    comment = Column(String(1024), nullable=True)
    
    algorithm_version = Column(String(50), default="1.0.0")
    model_version = Column(String(50), default="1.0.0")
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    project = relationship("Project")
    recommendation = relationship("ColorRecommendation")

class MLExperiment(Base):
    __tablename__ = "ml_experiments"

    id = Column(Integer, primary_key=True, index=True)
    model_type = Column(String(100)) # Random Forest, KNN, SVM, Logistic Regression
    accuracy = Column(Float)
    precision = Column(Float)
    recall = Column(Float)
    f1_score = Column(Float)
    
    parameters = Column(String(1024))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
