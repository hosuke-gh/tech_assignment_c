# ============================
# README.md
# ============================
"""
Animal Picture App (Python)

A Python-based microservice that fetches random pictures of animals (cats, dogs, bears), stores them in a database, and exposes REST APIs.

Tech Stack
- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite (embedded)
- Docker

How to Run (Without Docker)
---------------------------
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

How to Run (With Docker)
------------------------
docker build -t animal-picture-app-python .
docker run -p 8000:8000 animal-picture-app-python

APIs
----
POST /pictures
{
"animal": "cat",
"count": 2
}

GET /pictures/{animal}/last

Swagger UI
----------
http://localhost:8000/docs
"""