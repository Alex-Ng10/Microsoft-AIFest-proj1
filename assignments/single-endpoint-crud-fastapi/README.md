# 📘 Assignment: Single-Endpoint CRUD with FastAPI

## 🎯 Objective

Implement and validate a single CRUD endpoint in FastAPI to practice request validation, correct HTTP status codes, and quick manual testing.

## 🧭 Prerequisites

- Python 3.8+
- Basic familiarity with Python functions and JSON

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

### 🛠️ Implement a single `/items` endpoint supporting POST and GET

#### Description
Create an endpoint that allows clients to create an item (`POST /items`) and list items (`GET /items`). Use an in-memory list for storage.

#### Requirements

- `POST /items` accepts JSON `{ "name": "...", "description": "..." }` and returns the created item with an `id` and status `201`.
- `GET /items` returns a list of all items.
- Validate input using Pydantic models; `name` is required and must be non-empty.
- Return appropriate status codes (400 for invalid input, 201 on creation).

#### Example

Request:

```http
POST /items
Content-Type: application/json

{ "name": "Notebook", "description": "A ruled notebook" }
```

Response (201):

```json
{ "id": 1, "name": "Notebook", "description": "A ruled notebook" }
```

## 📤 Submission

- Submit your `starter-code.py` with the implemented endpoint.

## ✅ Grading Criteria

- Correct request validation and response codes: 60%
- Code clarity and concise comments: 40%

## 🔗 Resources

- FastAPI request bodies and Pydantic: https://fastapi.tiangolo.com/tutorial/body/
