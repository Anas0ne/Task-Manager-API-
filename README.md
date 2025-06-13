Here's your updated README file with JWT Authentication included:

---

# 🧠 Task Manager API (Django REST Framework)

This is a simple backend API built with Django and Django REST Framework. It’s a beginner-friendly project for learning how to build, secure, and test CRUD operations using REST APIs.

There’s no frontend — all testing is done through **Postman** or other API tools.

---

## 🔧 Features

* **User Authentication with JWT**
* View all tasks (authenticated users only)
* View a single task by ID
* Create a new task
* Update an existing task
* Delete a task
* Custom error handling for missing fields or invalid IDs

---

## 🛠 Stack

* Python
* Django
* Django REST Framework
* djangorestframework-simplejwt (for JWT authentication)
* Postman (for testing)

---

## 🚀 How to Run Locally

git clone <your-repo-url>
cd task_api
pip install -r requirements.txt
python manage.py runserver


---

## 🔐 Authentication

This API uses **JWT (JSON Web Tokens)** for authentication.

### Obtain Token:

POST /api/token/


**Body (JSON):**

{
  "username": "your_username",
  "password": "your_password"
}


### Refresh Token:

POST /api/token/refresh/


**Body (JSON):**

{
  "refresh": "your_refresh_token"
}


Use the **access token** in the `Authorization` header for all authenticated requests:


  -> Authorization: Bearer your_access_token


---

## 📮 API Endpoints

| Method | Endpoint                | Description              |
| ------ | ----------------------- | ------------------------ |
| GET    | /api/tasks/             | List all tasks           |
| GET    | /api/tasks/<id>/        | Retrieve a single task   |
| POST   | /api/tasks/create/      | Create a new task        |
| PUT    | /api/tasks/update/<id>/ | Update an existing task  |
| DELETE | /api/tasks/delete/<id>/ | Delete a task            |
| POST   | /api/token/             | Get JWT access/refresh   |
| POST   | /api/token/refresh/     | Refresh JWT access token |

> ⚠️ All task endpoints require JWT authentication.

---

## 🧪 Test with Postman

1. Run the server:

   python manage.py runserver
   

2. Use Postman to:

   * Authenticate and obtain a JWT token via `/api/token/`
   * Set the token in the `Authorization` header (Bearer Token)
   * Test all task endpoints

---

## 📌 Notes

* This project is designed for learning — user-based task ownership may be added later.
* Error messages are returned for invalid inputs, authentication issues, or non-existing task IDs.
* Only authenticated users can interact with task endpoints.




