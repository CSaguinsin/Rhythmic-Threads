# Test if app starts without errors
def test_app_health(client):
    response = client.get("/")
    assert response.status_code == 200
