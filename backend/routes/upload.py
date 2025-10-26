# upload.py
# FastAPI route for file upload

import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import UploadedFile

import shutil
from datetime import datetime

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'uploaded_files')
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/upload-document")
def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Generate a unique system filename
    system_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, system_filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        file_size = os.path.getsize(file_path)
        uploaded_at = datetime.now()
        # Store metadata in DB
        uploaded_file = UploadedFile(
            original_filename=file.filename,
            system_filename=system_filename,
            file_size_bytes=file_size,
            uploaded_at=uploaded_at
        )
        db.add(uploaded_file)
        db.commit()
        db.refresh(uploaded_file)
        return {"success": True, "message": "File uploaded successfully."}
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
