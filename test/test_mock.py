from fastapi.testclient import TestClient
from main import app, return_double

client = TestClient(app)

def test_return_square(mocker):
    mocker.patch(
        "main.get_double", # A la place de chercher la méthode get_double()
        return_value = 10
        )
    result = 10
    response = client.get("/5")
    assert result == response.json()
    assert response.status_code == 200