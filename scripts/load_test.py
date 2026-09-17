# locustfile.py
import random
from locust import HttpUser, task, between

class HousePriceUser(HttpUser):
    # Simulates a user waiting 1-3 seconds between requests
    # For maximum stress, change to constant(0) to remove waiting
    wait_time = between(1, 3)

    @task
    def predict_price(self):
        # Generate random features within the ranges you defined in Pydantic
        payload = {
            "MedInc": round(random.uniform(0.5, 15.0), 2),
            "HouseAge": round(random.uniform(1.0, 52.0), 1),
            "AveRooms": round(random.uniform(2.0, 10.0), 2),
            "AveBedrms": round(random.uniform(0.8, 3.0), 2),
            "Population": round(random.uniform(100.0, 3000.0), 0),
            "AveOccup": round(random.uniform(1.0, 6.0), 2),
            "Latitude": round(random.uniform(32.0, 42.0), 2),
            "Longitude": round(random.uniform(-125.0, -114.0), 2),
        }
        self.client.post("/predict", json=payload)