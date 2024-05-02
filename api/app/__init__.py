import os

from apiflask import APIFlask


def create_app():
    app = APIFlask(
        __name__, title="Rhythmic Threads API", version="0.1.0", docs_path="/"
    )

    # load config
    with app.app_context():
        app.config.from_pyfile("config.py", silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Swagger UI configuration
    app.info = {
        "description": "API documentation for interacting with Rhythmic Threads API",
        "contact": {
            "name": "API Support",
            "url": "https://m.me/jhdcruz",
            "email": "jhdcruz@proton.me",
        },
        "license": {
            "name": "Licensed under Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
    }

    from app.db import close_db
    from app.commands import setup_db_cmd, seed_db_cmd, create_user_cmd

    with app.app_context():
        app.teardown_appcontext(close_db)
        app.cli.add_command(setup_db_cmd)
        app.cli.add_command(seed_db_cmd)
        app.cli.add_command(create_user_cmd)

    # Blueprints / Routes
    from app.routes import auth, products, cart

    app.register_blueprint(auth.bp)
    app.register_blueprint(products.bp)
    app.register_blueprint(cart.bp)

    # don't run app in production server deployments
    if __name__ == "__main__":
        app.run()

    return app
