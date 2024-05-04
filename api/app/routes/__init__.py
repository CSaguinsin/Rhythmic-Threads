from datetime import datetime

from apiflask import HTTPTokenAuth, abort
from flask_jwt_extended import decode_token

from app import jwt
from app.db import get_db
from app.models.user import UserResponse

auth_token = HTTPTokenAuth(scheme='Bearer')


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user["username"]


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup,
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]

    try:
        db = get_db()
        user = db.execute(
            "SELECT id, username, name, created FROM rt_users WHERE username = ?", (identity,)
        ).fetchone()

        return UserResponse().dump(user)
    except Exception as e:
        abort(500, message="An error occurred while looking up the user.", detail=str(e))


@auth_token.verify_token
def verify_token(token):
    """
    Verify token and get user
    :param token:
    :return:
    """

    try:
        # check if the jwt token is still fresh
        decoded_token = decode_token(token, allow_expired=True)
        user_id = decoded_token["sub"]
        exp = decoded_token["exp"]

        # check if the token has expired
        expired = datetime.fromtimestamp(exp) < datetime.now()

        if not expired:
            db = get_db()
            user = db.execute(
                "SELECT id, username, created, updated FROM rt_users WHERE username = ?", (user_id,)
            ).fetchone()

            if user is None:
                abort(401, message="User not found.")
            else:
                return UserResponse().dump(user)
        else:
            abort(401, message="Token has expired. Please log in again.")

    except Exception as e:
        abort(
            500,
            message="An error occurred while verifying token.",
            detail=str(e)
        )
