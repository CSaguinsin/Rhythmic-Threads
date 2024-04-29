import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def setup_db():
    """
    Create the database from the schema.sql file.

    :return:
    """

    db = get_db()

    with current_app.open_resource("sql/schema.sql") as f:
        db.executescript(f.read().decode("utf8"))

    db.commit()


@click.command("setup-db")
@with_appcontext
def setup_db_cmd():
    """
    Creates a CLI command to initialize the database.

    Ex: flask --app api setup-db

    :return:
    """
    setup_db()
    click.echo("Initialized the database.")


@click.command("seed-db")
@click.option("--count", default=5)
@with_appcontext
def seed_db_cmd(count):
    """
    Creates a CLI command to seed the database with sample data.

    Ex: flask --app api seed-db

    :return:
    """
    from app.sql.seed_products import seed_products

    seed_products(count)
    click.echo("Seeded the database with sample data.")


def setup_app(app):
    """
    Register database functions with the application instance.
    :param app:
    :return:
    """

    app.teardown_appcontext(close_db)
    app.cli.add_command(setup_db_cmd)


def get_db():
    """
    Connect to the application's configured database.
    The connection is unique for each request and will be reused if
    this is called again.

    :return: sqlite3.Connection
    """

    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])

        # return rows that behave like dicts. This allows accessing the columns by name.
        g.db.row_factory = sqlite3.Row

    return g.db


# noinspection PyUnusedLocal
def close_db(e=None):
    """
    checks if a connection was created by checking if `g.db` was set.
    If the connection exists, it is closed.

    It is called after each request.

    :return:
    """

    db = g.pop("db", None)

    if db is not None:
        db.close()
