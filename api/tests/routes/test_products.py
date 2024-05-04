import pytest


@pytest.fixture()
def test_token(client):
    client.post(
        "/auth/register",
        json={
            "username": "test@test.com",
            "password": "test",
            "name": "Test User"
        })

    response = client.post(
        "/auth/login",
        json={
            "username": "test@test.com",
            "password": "test",
        })

    return response.json["token"]


def test_get_products(client):
    response = client.get("/products")
    assert response.status_code == 200


def test_create_product(test_token, client):
    response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "description": "This is a test product",
            "collection": "test",
            "category": "test",
            "sx": "M",
            "size": "M",
            "price": 100,
            "ratings": 4,
        },
        headers={"Authorization": f"Bearer {test_token}"}
    )
    assert response.status_code == 201


def test_update_product(test_token, client):
    response = client.patch(
        "/products/1",
        json={
            "name": "Test Product",
            "description": "This is a test product",
            "collection": "test",
            "category": "test",
            "sx": "M",
            "size": "M",
            "price": 100,
            "ratings": 4,
        },
        headers={"Authorization": f"Bearer {test_token}"}
    )
    assert response.status_code == 200


def test_delete_product(test_token, client):
    response = client.delete("/products/1", headers={"Authorization": f"Bearer {test_token}"})
    assert response.status_code == 200


def test_get_product_by_id(client):
    response = client.get("/products/2")
    assert response.status_code == 200
