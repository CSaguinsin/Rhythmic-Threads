# Test if app starts without errors
def test_app_health(client):
    """
    Test if the app starts without errors.

    :param client: Flask test client fixture
    """
    response = client.get("/")
    assert response.status_code == 200


def test_db_seed(cli):
    """
    Test if the database can be seeded with sample data.
    Checks if data insertion works.

    :param cli: Flask CLI runner fixture
    """
    from app.commands import seed_db_cmd

    result = cli.invoke(seed_db_cmd)
    assert "Seeded the database with sample data." in result.output
    assert result.exit_code == 0
