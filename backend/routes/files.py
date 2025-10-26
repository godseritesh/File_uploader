# files.py
# FastAPI route to list uploaded files metadata

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import UploadedFile

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.get("/files")
def list_files(db: Session = Depends(get_db)):
    files = db.query(UploadedFile).order_by(UploadedFile.uploaded_at.desc()).all()
    return [
        {
            "original_filename": f.original_filename,
            "system_filename": f.system_filename,
            "file_size_bytes": f.file_size_bytes,
            "uploaded_at": f.uploaded_at.isoformat(sep=' ', timespec='seconds')
        }
        for f in files
    ]
