from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from app.api.routes import auth, projects, images, analysis, colors, recolor, export, research
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

storage_dir = os.path.join(os.path.dirname(__file__), "storage")
os.makedirs(storage_dir, exist_ok=True)
app.mount("/storage", StaticFiles(directory=storage_dir), name="storage")

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(projects.router, prefix=f"{settings.API_V1_STR}/projects", tags=["projects"])
app.include_router(images.router, prefix=f"{settings.API_V1_STR}/images", tags=["images"])
app.include_router(analysis.router, prefix=f"{settings.API_V1_STR}/analysis", tags=["analysis"])
app.include_router(colors.router, prefix=f"{settings.API_V1_STR}/colors", tags=["colors"])
app.include_router(recolor.router, prefix=f"{settings.API_V1_STR}/recolor", tags=["recolor"])
app.include_router(export.router, prefix=f"{settings.API_V1_STR}/export", tags=["export"])
app.include_router(research.router, prefix=f"{settings.API_V1_STR}/research", tags=["research"])

from app.api.routes import stats
app.include_router(stats.router, prefix=f"{settings.API_V1_STR}/stats", tags=["stats"])

@app.get("/")
def root():
    return {"message": "Welcome to AI Color Designer API"}
