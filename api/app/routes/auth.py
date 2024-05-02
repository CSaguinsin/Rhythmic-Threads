from apiflask import APIBlueprint, abort
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

from app import auth
from app.db import get_db, close_db
from app.models.generic import GenericResponse
from app.models.user import UserRequest, UserResponse, UserLoginRequest

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
@bp.output(UserResponse, 200)
@bp.doc(
    summary="Login a user",
    description="Login a user with an username and password.",
)
def login(json_data):
    username = json_data["username"]
    password = json_data["password"]

    try:
        user = verify_password(username, password)
        session["user"] = user
        return user
    except Exception as e:
        abort(500, message="An error occurred while logging in the user.", detail=e)


@bp.get("/logout")
@bp.output(GenericResponse, 200)
@bp.auth_required(auth)
@bp.doc(
    summary="Logout current user",
    description="This requires manual clearing of session cookies from client browser.",
)
def logout():
    session.clear()
    return GenericResponse().dump(
        {"message": f"User {auth.current_user['username']} successfully logged out."}
    )


@bp.get("/user")
@bp.output(UserResponse, 200)
@bp.auth_required(auth)
@bp.doc(summary="Get currently logged-in user information")
def user_session():
    try:
        return UserResponse().dump(auth.current_user)
    except Exception as e:
        abort(
            500,
            message="An error occurred while fetching the user's information",
            detail=e,
        )


@auth.verify_password
def verify_password(username, password):
    """
    Verify the user's password.
    This is used by the HTTPBasicAuth.verify_password decorator.

    This 2-params function is required for the HTTPBasicAuth.verify_password decorator.

    :param username:
    :param password:
    :return:
    """
    db = get_db()
    error = None

    try:
        if not username:
            error = "Email is required."
        elif not password:
            error = "Password is required."

        if error is None:
            user_requested = db.execute(
                "SELECT id, name, username, password FROM rt_users WHERE username = ?", (username,)
            ).fetchone()

            if user_requested is None or not check_password_hash(
                user_requested["password"], password
            ):
                abort(401, "Incorrect username or password.")
            else:
                return UserResponse().dump(user_requested)
        else:
            # If user or password is missing
            abort(401, error)

    except Exception as e:
        # Unknown error
        abort(
            500,
            message="An error occurred while logging in the user.",
            detail=e,
        )

    finally:
        close_db()
