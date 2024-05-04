from datetime import timedelta

from apiflask import APIBlueprint, abort
from flask import jsonify
from flask_jwt_extended import create_access_token, get_current_user, jwt_required
from marshmallow.fields import String
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import get_db, close_db
from app.models.generic import GenericResponse
from app.models.user import UserRequest, UserLoginRequest, UserResponse
from app.routes import auth_token, verify_token

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
