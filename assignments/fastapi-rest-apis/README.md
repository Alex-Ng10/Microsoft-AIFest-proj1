# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple RESTful API using the FastAPI framework to practice route design, request/response handling, and basic data validation.

## 🧭 Prerequisites

- Python 3.8+
- Basic knowledge of Python functions and data structures

## ⚙️ Setup

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the starter app:

```bash
uvicorn starter-code:app --reload
```

## 📝 Tasks

### 🛠️ Implement a Notes API

#### Description
Create a small API to create, list, retrieve, update, and delete text notes. Store notes in an in-memory list for this exercise.

#### Requirements

- `GET /notes` — return a list of notes.
- `POST /notes` — create a new note with a JSON body: `{ "title": "...", "content": "..." }`. Respond with the created note and its id.
- `GET /notes/{id}` — return the note with the given id or 404 if not found.
- `PUT /notes/{id}` — update an existing note's title and content.
- `DELETE /notes/{id}` — delete the note and return a 204 status on success.
- Use Pydantic models for request validation.

#### Example

Request:

```http
POST /notes
Content-Type: application/json

{ "title": "Shopping", "content": "Milk, eggs" }
```

Response:

```json
{ "id": 1, "title": "Shopping", "content": "Milk, eggs" }
```

## 📤 Submission

- Submit the modified `starter-code.py` with your implementation.
- Include any additional modules you create in the same folder.

## ✅ Grading Criteria

- Correct API behavior and HTTP status codes: 50%
- Input validation using Pydantic: 20%
- Code clarity and comments: 20%
- Bonus: add filtering or pagination on `GET /notes`: 10%

## 🔗 Resources

- FastAPI docs: https://fastapi.tiangolo.com/
- Uvicorn docs: https://www.uvicorn.org/

Good luck — ask for a hint if you get stuck!
