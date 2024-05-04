from datetime import datetime, timedelta

from apiflask import APIBlueprint, abort
from flask import jsonify
from flask_jwt_extended import create_access_token, decode_token, get_current_user, jwt_required
from marshmallow.fields import String
from werkzeug.security import generate_password_hash, check_password_hash

from app import jwt
from app.db import get_db, close_db
from app.models.generic import GenericResponse
from app.models.user import UserRequest, UserLoginRequest, UserResponse
from app.routes import auth_token

bp = APIBlueprint("auth", __name__, url_prefix="/auth")


@bp.post("/register")
@bp.input(UserRequest, location="json")
@bp.output(GenericResponse, 201)
@bp.doc(summary="Register a new user")
def register(json_data):
    username = json_data["username"]
    password = json_data["password"]
    name = json_data["name"]

    db = get_db()
    error = None

    try:
        if not username:
            error = "Email is required."
        elif not password:
            error = "Password is required."
        elif not name:
            name = None

        if error is None:
            db.execute(
                "INSERT INTO rt_users (username, name, password) VALUES (?, ?, ?)",
                (username, name, generate_password_hash(password)),
            )
            db.commit()
            return GenericResponse().dump(
                {"message": f"User {username} successfully registered."}
            )
        else:
            # If user or password is missing
            abort(401, error)
    except db.IntegrityError:
        abort(400, f"User {username} is already registered.")
    except Exception as e:
        # Unknown error
        abort(500, str(e.__cause__))
    finally:
        close_db()


@bp.post("/login")
@bp.input(UserLoginRequest, location="json")
@bp.output({"token": String()}, 200)
@bp.doc(summary="Login a user")
def login(json_data):
    username = json_data["username"]
    password = json_data["password"]

    db = get_db()

    try:
        # Get user from database
        user = db.execute(
            "SELECT id, username, password, created, updated FROM rt_users WHERE username = ?", (username,)
        ).fetchone()

        # check password hash
        if user is not None:
            if check_password_hash(user["password"], password):
                # Create a new access token that expires in 24 hours
                token = create_access_token(identity=user, expires_delta=timedelta(days=1))

                verify_token(token)

                return jsonify({"token": token})
            else:
                abort(401, message="Invalid password.")

    except Exception as e:
        abort(500, message="An error occurred while logging in the user.", detail=str(e))
    finally:
        close_db()


@bp.get("/profile")
@bp.output(UserResponse, 200)
@bp.auth_required(auth_token)
@jwt_required()
@bp.doc(summary="Get currently logged-in user profile")
def profile():
    user = get_current_user()

    if user is not None:
        return UserResponse().dump(user)
    else:
        abort(401, message="User not logged in.")


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup,
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    db = get_db()

    try:
        user = db.execute(
            "SELECT id, username, name, created FROM rt_users WHERE username = ?", (identity,)
        ).fetchone()

        return UserResponse().dump(user)
    except Exception as e:
        abort(500, message="An error occurred while looking up the user.", detail=str(e))
    finally:
        close_db()


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user["username"]


@auth_token.verify_token
def verify_token(token):
    """
    Verify token and get user
    :param token:
    :return:
    """
    db = get_db()

    try:
        # check if the jwt token is still fresh
        decoded_token = decode_token(token, allow_expired=True)
        user_id = decoded_token["sub"]
        exp = decoded_token["exp"]

        # check if the token has expired
        expired = datetime.fromtimestamp(exp) < datetime.now()

        if not expired:
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

    finally:
        close_db()
