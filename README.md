## Animal Picture App (Python)

A Python-based microservice that fetches random pictures of animals (cats, dogs, bears), stores them in a database, and exposes REST APIs.

Tech Stack
- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite (embedded)
- Docker

## How to Run (Without Docker)
---------------------------
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

## How to Run (With Docker)
------------------------
docker build -t animal-picture-app-python .
docker run -p 8000:8000 animal-picture-app-python

## APIs
----
POST /pictures
{
"animal": "dog",
"count": 2
}

GET /pictures/{animal}/last

## Swagger UI
----------
http://localhost:8000/docs
"""

## Test the fetch API call
----
source venv/bin/activate
pytest

## For future test expansion
Add nominal case test for POST call
Add multiple animals of the same type for POST call
Add invalid animal for POST call
Add index overflow for GET call

## For even further future expansion
Port to Java