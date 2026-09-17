from fastapi.testclient import TestClient
from house_price.api.main import app

client = TestClient(app)

def test_home():
    r = client.get("/")
    assert r.status_code == 200

def test_predict():
    payload = {
        "MedInc": 5.0, "HouseAge": 20.0, "AveRooms": 5.0, "AveBedrms": 1.0,
        "Population": 1000.0, "AveOccup": 3.0, "Latitude": 34.0, "Longitude": -118.0,
    }
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    assert "predicted_price" in r.json()