import os
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import uuid

from app.api.dependencies import get_db
from app.api.routes.projects import get_current_user
from app.models.user import User
from app.models.project import Project
from app.core.config import settings

router = APIRouter()
EXPORT_DIR = Path(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "storage", "exports"))
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

@router.get("/{project_id}/pdf")
def export_project_pdf(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = db.query(Project).filter(Project.id == project_id, Project.user_id == current_user.id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    pdf_filename = f"report_{project.id}_{uuid.uuid4().hex[:8]}.pdf"
    pdf_path = EXPORT_DIR / pdf_filename

    # Create a simple PDF for the thesis demonstration
    c = canvas.Canvas(str(pdf_path), pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 24)
    c.drawString(50, height - 80, "AI Color Designer - Project Report")
    
    c.setFont("Helvetica", 14)
    c.drawString(50, height - 120, f"Project Name: {project.name}")
    c.drawString(50, height - 140, f"Design Style: {project.design_style or 'N/A'}")
    c.drawString(50, height - 160, f"Mood Goal: {project.mood_goal or 'N/A'}")
    c.drawString(50, height - 180, f"Created At: {project.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
    
    c.drawString(50, height - 220, "Summary:")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 240, "This report contains the AI-based analysis, segmentation results,")
    c.drawString(50, height - 255, "and color harmonization recommendations for the selected object.")
    
    # In a full implementation, you'd draw the original and recolored images onto the PDF
    
    c.save()
    
    return FileResponse(
        path=str(pdf_path),
        filename=f"{project.name}_Report.pdf",
        media_type="application/pdf"
    )
