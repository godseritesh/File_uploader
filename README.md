# File Uploader and Tracker

## Overview
A simple, production-ready web application for uploading and tracking files. Built with FastAPI, SQLAlchemy, SQLite, and a modern HTML/CSS/JS frontend.

## Features
- Upload any file type and store it securely with a unique name
- Track all uploads with metadata (original name, size, upload time)
- View upload history in a responsive, user-friendly table
- Clean, modern UI with clear call-to-actions

## Tech Stack
- Backend: FastAPI, SQLAlchemy ORM, SQLite
- Frontend: HTML, CSS, JavaScript (no frameworks)

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
