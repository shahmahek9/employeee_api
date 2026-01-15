from fastapi.testclient import TestClient
from app.main import app



client = TestClient(app)

def get_token():
    response = client.post(
        "/api/token",
        params={"username": "admin", "password": "admin123"}
    )
    return response.json()["access_token"]
def test_create_employee():
    token = get_token()
    response = client.post(
        "/api/employees/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Test User",
            "email": "testuser@example.com",
            "department": "IT",
            "role": "Developer"
        }
    )
    assert response.status_code == 201
    assert response.json()["email"] == "testuser@example.com"
def test_duplicate_email():
    token = get_token()
    response = client.post(
        "/api/employees/",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "name": "Test User 2",
            "email": "testuser@example.com"
        }
    )
    assert response.status_code == 400
def test_list_employees():
    token = get_token()
    response = client.get(
        "/api/employees/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
def test_get_invalid_employee():
    token = get_token()
    response = client.get(
        "/api/employees/9999",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 404
