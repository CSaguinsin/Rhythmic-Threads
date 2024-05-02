from apiflask import APIBlueprint, abort, HTTPBasicAuth
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db, close_db
from app.models.generic import GenericResponse
from app.models.user import UserRequest, UserResponse

bp = APIBlueprint("auth", __name__, url_prefix="/auth")
auth = HTTPBasicAuth()


@bp.post("/register")
@bp.input(UserRequest, location="json")
@bp.output(GenericResponse, 201)
@bp.doc(summary="Register a new user")
def register(json_data):
    email = json_data["email"]
    password = json_data["password"]
    name = json_data["name"]

    db = get_db()
    error = None

    try:
        if not email:
            error = "Email is required."
        elif not password:
            error = "Password is required."
        elif not name:
            name = None

        if error is None:
            db.execute(
                "INSERT INTO rt_users (email, name, password) VALUES (?, ?, ?)",
                (email, name, generate_password_hash(password)),
            )
            db.commit()
            return GenericResponse().dump(
                {"message": f"User {email} successfully registered."}
            )
        else:
            # If user or password is missing
            abort(401, error)
    except db.IntegrityError:
        abort(400, f"User {email} is already registered.")
    except Exception as e:
        # Unknown error
        abort(500, str(e.__cause__))
    finally:
        close_db()


@bp.post("/login")
@bp.input(UserRequest, location="json")
@bp.output(UserResponse, 200)
@auth.verify_password
@bp.doc(
    summary="Login a user",
    description="Login a user with an email and password.",
)
def login(json_data):
    email = json_data["email"]
    password = json_data["password"]

    db = get_db()
    error = None

    try:
        if not email:
            error = "Email is required."
        elif not password:
            error = "Password is required."

        if error is None:
            user_requested = db.execute(
                "SELECT id, name, email, password FROM rt_users WHERE email = ?", (email,)
            ).fetchone()

            if user_requested is None or not check_password_hash(
                user_requested["password"], password
            ):
                abort(401, "Incorrect username or password.")
            else:
                session["user"] = UserResponse().dump(user_requested)

                # return a 200 status code on successful login
                return UserResponse().dump(user_requested)
        else:
            # If user or password is missing
            abort(401, error)
    finally:
        close_db()


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
        {"message": f"User {auth.current_user['email']} successfully logged out."}
    )


@bp.get("/user")
@bp.output(UserResponse, 200)
@bp.auth_required(auth)
@bp.doc(summary="Get currently logged-in user information")
def user_session():
    return UserResponse().dump(auth.current_user)
