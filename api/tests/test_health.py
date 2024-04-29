from app.db import setup_db_cmd


# Test if app starts without errors
def test_app_health(client):
    response = client.get("/")
    assert response.status_code == 200


def test_db_setup(cli):
    result = cli.invoke(setup_db_cmd)
    assert "Initialized the database." in result.output
    assert result.exit_code == 0
