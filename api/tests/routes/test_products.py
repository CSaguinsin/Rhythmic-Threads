def test_get_products(client):
    response = client.get("/products")
    assert response.status_code == 200


def test_create_product(client):
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
    )
    assert response.status_code == 201


def test_update_product(client):
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
    )
    assert response.status_code == 200


def test_delete_product(client):
    response = client.delete("/products/1")
    assert response.status_code == 200


def test_get_product_by_id(client):
    response = client.get("/products/2")
    assert response.status_code == 200
