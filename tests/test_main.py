# ============================
# test_main.py
# ============================
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_fetch_cat():
    response = client.post("/pictures", json={"animal": "cat", "count": 1})
    assert response.status_code == 200
