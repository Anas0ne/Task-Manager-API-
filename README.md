# 🧠 Task Manager API (Django REST Framework)

This is a simple backend API built with Django and Django REST Framework. It’s a beginner-friendly project for learning how to build, test, and handle CRUD operations using REST APIs.

There’s no frontend — all testing is done through **Postman** or other API tools.

---

## 🔧 Features

- View all tasks
- View a single task by ID
- Create a new task
- Update an existing task
- Delete a task
- Custom error handling for missing fields or invalid IDs

---

## 🛠 Stack

- Python
- Django
- Django REST Framework
- Postman (for testing)

---

## 🚀 How to Run Locally

git clone <your-repo-url>
cd task_api
pip install -r requirements.txt
python manage.py runserver

---


📮 API Endpoints
Method	  Endpoint	                  Description
GET	    /api/tasks/	                List all tasks
GET	    /api/tasks/<id>/	          Retrieve a single task
POST	  /api/tasks/create/	        Create a new task
PUT	    /api/tasks/update/<id>/    	Update an existing task
DELETE	/api/tasks/delete/<id>/    	Delete a task

---

🧪 Test with Postman
After running the server (python manage.py runserver), you can use Postman to hit the endpoints and test task creation, updates, and deletions.

---

📌 Notes
This project is meant for learning — no authentication or user-based task ownership yet.

Error messages are returned for invalid inputs or non-existing task IDs.


