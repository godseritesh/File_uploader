# upload.py
# FastAPI route for file upload

import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from fastapi.responses import JSONResponse
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
    # Limit file size to 10MB
    MAX_SIZE = 10 * 1024 * 1024
    if file.content_type is None or file.content_type == "application/octet-stream":
        return JSONResponse(status_code=400, content={"success": False, "message": "Unsupported or missing file type."})
    # Read file in chunks to check size
    system_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, system_filename)
    size = 0
    try:
        with open(file_path, "wb") as buffer:
            while True:
                chunk = file.file.read(1024 * 1024)
                if not chunk:
                    break
                size += len(chunk)
                if size > MAX_SIZE:
                    buffer.close()
                    os.remove(file_path)
                    return JSONResponse(status_code=413, content={"success": False, "message": "File too large (max 10MB)."})
                buffer.write(chunk)
        uploaded_at = datetime.now()
        uploaded_file = UploadedFile(
            original_filename=file.filename,
            system_filename=system_filename,
            file_size_bytes=size,
            uploaded_at=uploaded_at
        )
        db.add(uploaded_file)
        db.commit()
        db.refresh(uploaded_file)
        return {"success": True, "message": "File uploaded successfully."}
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        return JSONResponse(status_code=500, content={"success": False, "message": f"Server error: {str(e)}"})
