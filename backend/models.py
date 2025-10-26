# models.py
# SQLAlchemy ORM model for uploaded files

from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
import datetime

class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True)
    original_filename = Column(String, nullable=False)
    system_filename = Column(String, nullable=False, unique=True)
    file_size_bytes = Column(Integer, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.datetime.utcnow)
