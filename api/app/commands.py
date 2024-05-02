import click
from flask.cli import with_appcontext


@click.command("setup-db")
@with_appcontext
def setup_db_cmd():
    """
    Creates a CLI command to initialize the database.

    Ex: flask --app api setup-db

    :return:
    """
    from db import setup_db

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


@click.command("create-user")
@click.option("--user", prompt="Enter username")
@click.option("--pw", prompt="Enter password", hide_input=True, confirmation_prompt=True)
@click.option("--name", prompt="Enter full name", required=False)
@with_appcontext
def create_user_cmd(user, pw, name):
    """
    Creates a CLI command to create a new user.

    Ex: flask --app api create-user

    :param user:
    :param pw:
    :param name:
    :return:
    """
    from db import get_db
    from app.models.user import UserRequest

    db = get_db()

    try:
        user_data = UserRequest().load({"username": user, "password": pw, "name": name})
        db.execute(
            "INSERT INTO rt_users (username, password, name) VALUES (?, ?, ?)",
            (user_data["username"], user_data["password"], user_data["name"]),
        )
        db.commit()
        click.echo(f"User {user} created successfully.")
    except Exception as e:
        click.echo(f"Failed to create user {user}.")
        click.echo(str(e))
    finally:
        db.close()
