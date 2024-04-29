def test_get_products(client):
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json == []


def test_get_new_arrivals(client):
    response = client.get("/products/new-arrivals")
    assert response.status_code == 200
    assert response.json == []


def test_get_products_by_rating(client):
    response = client.get("/products/5")
    assert response.status_code == 200
    assert response.json == []


def test_get_products_by_category(client):
    response = client.get("/products/clothing")
    assert response.status_code == 200
    assert response.json == []
