import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash


@click.command("setup-db")
@with_appcontext
def setup_db_cmd():
    """
    Creates a CLI command to initialize the database.

    Ex: flask --app api setup-db

    :return:
    """
    from app.db import setup_db

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
@click.option("--username", prompt="Enter username")
@click.option("--pw", prompt="Enter password", hide_input=True, confirmation_prompt=True)
@click.option("--name", prompt="Enter full name", required=False)
@with_appcontext
def create_user_cmd(username, pw, name):
    """
    Creates a CLI command to create a new user.

    Ex: flask --app api create-user

    :param username:
    :param pw:
    :param name:
    :return:
    """
    from app.db import get_db
    from app.models.user import UserRequest

    db = get_db()

    try:
        user_data = UserRequest().load({"username": username, "password": pw, "name": name})
        hashed_pw = generate_password_hash(user_data["password"])

        db.execute(
            "INSERT INTO rt_users (username, password, name) VALUES (?, ?, ?)",
            (user_data["username"], hashed_pw, user_data["name"]),
        )

        db.commit()
        click.echo(f"User {username} created successfully.")

    except Exception as e:
        click.echo(f"Failed to create user {username}.")
        click.echo(e)

    finally:
        db.close()
