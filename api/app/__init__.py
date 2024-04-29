import os

from apiflask import APIFlask


def create_app(temp_config=None):
    app = APIFlask(
        __name__, title="Rhythmic Threads API", version="0.1.0", docs_path="/"
    )

    # Default configs
    app.url_map.strict_slashes = False
    app.secret_key = app.config.get("SECRET_KEY")
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "rt_dev.sqlite")
    )

    if temp_config is None:
        # load the default config, if it exists
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in, for custom values
        app.config.from_mapping(temp_config)

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

    from . import db

    db.setup_app(app)

    from app.sql.seed_products import seed_products

    # Seed sample data when SEED is configured in env
    if app.config.from_mapping(SEED=True):
        with app.app_context():
            seed_products(count=5)

    # Blueprints / Routes
    from .routes import auth
    from .routes import products

    app.register_blueprint(auth.bp)
    app.register_blueprint(products.bp)

    # don't run app in production server deployments
    if __name__ == "__main__":
        app.run(debug=app.config.get("DEBUG", True))

    return app
