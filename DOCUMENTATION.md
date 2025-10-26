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

## API Examples

### POST /upload-document
**Description:** Upload a file.

**Request:**
```
POST http://localhost:8000/upload-document
Content-Type: multipart/form-data
file: <your file>
```
**Response (success):**
```
{
	"success": true,
	"message": "File uploaded successfully."
}
```
**Response (error):**
```
{
	"success": false,
	"message": "File too large (max 10MB)."
}
```

### GET /files
**Description:** List all uploaded files and their metadata.

**Request:**
```
GET http://localhost:8000/files
```
**Response:**
```
[
	{
		"original_filename": "example.txt",
		"system_filename": "uuid_example.txt",
		"file_size_bytes": 1234,
		"uploaded_at": "2025-10-26 12:34:56"
	},
	...
]
```

## Troubleshooting

- **CORS errors:** Make sure the backend is running and accessible at the correct port (default: 8000).
- **File not uploading:** Check file size/type and ensure backend is running. Review browser console for errors.
- **Database errors:** Ensure you have write permissions in the project directory.
- **Frontend not updating:** Clear browser cache or do a hard refresh.

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


## Room for Improvement
If I had another day, I would focus on:

- **Adding automated tests (unit and integration):**
	- Write unit tests for backend routes and database logic using pytest.
	- Add integration tests to verify the complete upload and retrieval workflow.

- **Improving error handling and user feedback:**
	- Refine backend error responses for clarity and consistency.
	- Enhance frontend to display clear, actionable messages for upload failures, network issues, and invalid file types.

- **Enhancing accessibility:**
	- Add ARIA labels and roles for all interactive elements.
	- Improve keyboard navigation and ensure color contrast meets accessibility standards.

- **Expanding documentation with API examples and troubleshooting tips:**
	- Provide example requests and responses for each API endpoint.
	- Add a troubleshooting section for common setup and runtime issues.

- **Adding drag-and-drop upload:**
	- Implement a drag-and-drop area for file uploads to improve user experience.

- **Pagination for file history:**
	- Add pagination to the file history page to efficiently handle large numbers of uploads.

- **User authentication for better security:**
	- Add user registration and login features.
	- Restrict file upload and history access to authenticated users only.

## Author
Ritesh Sanjay Godse  
[Resume](https://shorturl.at/7l10g)
