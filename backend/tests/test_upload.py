import os
import tempfile
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_upload_document():
    # Create a temporary file to upload
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"test content")
        tmp.seek(0)
        tmp_name = tmp.name
    with open(tmp_name, "rb") as f:
        response = client.post("/upload-document", files={"file": (os.path.basename(tmp_name), f, "text/plain")})
    os.remove(tmp_name)
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_files_list():
    response = client.get("/files")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
