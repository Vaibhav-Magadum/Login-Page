import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_redirects_to_login(client):
    response = client.get("/")
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data


def test_register_page_loads(client):
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register" in response.data


def test_login_with_valid_credentials(client):
    response = client.post(
        "/login",
        data={"username": "admin", "password": "admin123"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Welcome" in response.data


def test_login_with_invalid_credentials(client):
    response = client.post(
        "/login",
        data={"username": "admin", "password": "wrong"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Invalid username or password" in response.data


def test_login_with_empty_fields(client):
    response = client.post(
        "/login",
        data={"username": "", "password": ""},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Please fill in all fields" in response.data


def test_register_new_user(client):
    response = client.post(
        "/register",
        data={
            "username": "newuser",
            "password": "pass123",
            "confirm_password": "pass123",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Registration successful" in response.data


def test_register_password_mismatch(client):
    response = client.post(
        "/register",
        data={
            "username": "newuser",
            "password": "pass123",
            "confirm_password": "different",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Passwords do not match" in response.data


def test_register_existing_user(client):
    response = client.post(
        "/register",
        data={
            "username": "admin",
            "password": "pass123",
            "confirm_password": "pass123",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Username already exists" in response.data


def test_dashboard_requires_login(client):
    response = client.get("/dashboard")
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_logout(client):
    # Log in first
    client.post("/login", data={"username": "admin", "password": "admin123"})
    # Then log out
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"You have been logged out" in response.data
