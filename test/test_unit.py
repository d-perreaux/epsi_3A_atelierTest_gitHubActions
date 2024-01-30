from fastapi.testclient import TestClient
import pytest
from main import app
from random import randint

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "hello World!"

def test_number():
    number = randint(1, 100)
    response = client.get(f"/{number}")
    assert response.status_code == 200
    assert response.json() == number * 2