# main.py
# FastAPI app entry point

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import upload, files
import os

# Create database tables if not exist
def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow CORS for local file access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(upload.router)
app.include_router(files.router)

@app.on_event("startup")
def on_startup():
    # Ensure upload directory exists
    upload_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'uploaded_files')
    os.makedirs(upload_dir, exist_ok=True)
    create_db_and_tables()
