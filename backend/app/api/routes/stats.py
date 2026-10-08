from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.api.dependencies import get_db
from app.api.routes.projects import get_current_user
from app.models.user import User
from app.models.project import Project
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/")
def get_user_stats(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # 1. Total projects/images
    total_projects = db.query(Project).filter(Project.user_id == current_user.id).count()
    
    # 2. Get all analysis data to calculate objects and colors
    projects = db.query(Project).filter(Project.user_id == current_user.id).all()
    
    total_objects = 0
    total_recommendations = 0
    
    for p in projects:
        if p.analysis_data:
            objects = p.analysis_data.get("objects", [])
            total_objects += len(objects)
            
            # Count color recommendations
            colors = p.analysis_data.get("color_recommendations", [])
            total_recommendations += len(colors)

    # 3. Dummy chart data (fallback if not enough data)
    # Ideally, we would group by created_at. Let's do a simple group by date
    chart_data = [
        {"name": "Dush", "images": 0, "objects": 0},
        {"name": "Sesh", "images": 0, "objects": 0},
        {"name": "Chor", "images": 0, "objects": 0},
        {"name": "Pay", "images": 0, "objects": 0},
        {"name": "Juma", "images": 0, "objects": 0},
        {"name": "Shan", "images": 0, "objects": 0},
        {"name": "Yak", "images": 0, "objects": 0},
    ]
    
    # If there is at least one project, let's put it in today's slot just for dynamic effect
    if total_projects > 0:
        import datetime
        today_idx = datetime.datetime.today().weekday()
        chart_data[today_idx]["images"] = total_projects
        chart_data[today_idx]["objects"] = total_objects

    # 4. Recent projects
    recent_projects_query = db.query(Project).filter(Project.user_id == current_user.id).order_by(Project.created_at.desc()).limit(5).all()
    recent_projects = []
    for p in recent_projects_query:
        objects_count = len(p.analysis_data.get("objects", [])) if p.analysis_data else 0
        recent_projects.append({
            "id": p.id,
            "name": p.name or f"Loyiha {p.id}",
            "date": p.created_at.strftime("%d %b, %H:%M") if p.created_at else "Bugun",
            "objects": objects_count,
            "status": "Yakunlangan" if p.modified_image_path else "Jarayonda"
        })

    return {
        "kpis": {
            "total_images": total_projects,
            "total_objects": total_objects,
            "total_recommendations": total_recommendations,
            "avg_mood": "85%" # Static for now since we don't have a numeric mood score in DB yet
        },
        "area_chart": chart_data,
        "recent_projects": recent_projects
    }
