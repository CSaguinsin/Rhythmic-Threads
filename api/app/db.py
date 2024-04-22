import sqlite3

import click
from flask import current_app, g


def init_db():
    """
    Create the database from the schema.sql file.

    :return:
    """

    db = get_db()

    with current_app.open_resource("sql/schema.sql") as f:
        db.executescript(f.read().decode("utf8"))

    db.commit()


@click.command("init-db")
def init_db_command():
    """
    Creates a CLI command to initialize the database.

    Ex: flask --app api init-db

    :return:
    """

    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    """
    Register database functions with the application instance.
    :param app:
    :return:
    """

    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def get_db():
    """
    Connect to the application's configured database.
    The connection is unique for each request and will be reused if
    this is called again.

    :return: sqlite3.Connection
    """

    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )

        # return rows that behave like dicts. This allows accessing the columns by name.
        g.db.row_factory = sqlite3.Row

    return g.db


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
