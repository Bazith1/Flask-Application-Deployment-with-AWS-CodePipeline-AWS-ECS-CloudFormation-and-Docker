import requests

def test_api_response():
    response = requests.get("http://localhost:5000/api/endpoint")
    assert response.status_code == 200
