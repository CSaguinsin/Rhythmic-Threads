import os
from datetime import datetime, timezone, timedelta

from apiflask import APIFlask
from flask_jwt_extended import JWTManager, get_jwt, get_jwt_identity, create_access_token, set_access_cookies, \
    jwt_required

jwt = JWTManager()


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

    jwt.init_app(app)

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

    # Using an `after_request` callback, we refresh any token that is within 30
    # minutes of expiring. Change the time deltas to match the needs of your application.
    @app.after_request
    @jwt_required
    def refresh_expiring_jwts(response):
        """
        Refresh the JWT token if it is within 10 minutes of expiring
        after each requests
        :param response:
        :return:
        """
        exp_timestamp = get_jwt()["exp"] or None

        if exp_timestamp is not None:
            try:
                now = datetime.now(timezone.utc)
                target_timestamp = datetime.timestamp(now + timedelta(minutes=10))
                if target_timestamp > exp_timestamp:
                    access_token = create_access_token(identity=get_jwt_identity())
                    set_access_cookies(response, access_token)
                return response
            except (RuntimeError, KeyError):
                # Case where there is not a valid JWT. Just return the original response
                return response

    # don't run app in production server deployments
    if __name__ == "__main__":
        app.run()

    return app
