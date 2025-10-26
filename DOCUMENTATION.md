# File Uploader and Tracker

## Introduction
This web application allows users to upload files and track their upload history. It is built with FastAPI, SQLAlchemy, SQLite, and a modern HTML/CSS/JS frontend. The project is modular, maintainable, and follows best practices for production-ready code.

## Features
- Upload any file type securely
- Files are stored with a unique system filename (UUID-based)
- Metadata (original filename, system filename, size, upload time) is stored in SQLite
- View upload history in a responsive, user-friendly table
- Clean, modern UI with clear call-to-actions

## How to Run
1. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
2. Start the backend server:
	```bash
	uvicorn backend.main:app --reload
	```
3. Open `frontend/index.html` in your browser to upload files.
4. Open `frontend/files.html` to view upload history.

## Project Structure
```
file_uploader/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── routes/
│   │   ├── upload.py
│   │   └── files.py
│
├── frontend/
│   ├── index.html
│   ├── files.html
│   ├── style.css
│
├── uploaded_files/  (auto-created if not exists)
│
├── requirements.txt
├── README.md
└── DOCUMENTATION.md
```

## Author
Ritesh Sanjay Godse  
[Resume](https://shorturl.at/7l10g)
