from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_urunleri_listele():
    response = client.get("/api/products")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 3