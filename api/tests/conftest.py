import os
import shutil

import pytest

from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "DEBUG": False,
        "TESTING": True,
        "DATABASE": os.path.join(app.instance_path, "rt_test.sqlite")
    })

    # init db
    with app.app_context():
        if not os.path.exists(app.config["DATABASE"]):
            from app.db import setup_db
            setup_db()

        from app.sql.seed_products import seed_products
        seed_products(count=5)

    yield app

    # clean db
    shutil.rmtree(app.config["DATABASE"], ignore_errors=True)


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def cli(app):
    return app.test_cli_runner()
