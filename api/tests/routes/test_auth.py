import pytest


@pytest.fixture()
def default_user(client):
    """
    Register a default user for testing.

    :param client:
    :return:
    """
    client.post(
        "/auth/register",
        json={
            "username": "admin@admin.com",
            "password": "admin",
            "name": "admin"
        })


def test_register(client):
    response = client.post(
        "/auth/register",
        json={
            "username": "admin2@admin.com",
            "password": "admin2",
            "name": "admin2"
        })
    assert response.status_code == 201


def test_login(default_user, client):
    response = client.post(
        "/auth/login",
        json={
            "username": "admin@admin.com",
            "password": "admin",
        })

    assert response.status_code == 200
