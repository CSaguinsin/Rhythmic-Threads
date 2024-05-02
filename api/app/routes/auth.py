from apiflask import APIBlueprint, abort, HTTPBasicAuth
from flask import session, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db, close_db
from ..models.generic import GenericResponse
from ..models.user import UserRequest, UserResponse

bp = APIBlueprint("auth", __name__, url_prefix="/auth")
auth = HTTPBasicAuth()


@bp.post("/register")
@bp.input(UserRequest, location="json")
@bp.output(GenericResponse, 201)
@bp.doc(summary="Register a new user")
def register(data):
    email = data["email"]
    password = data["password"]

    db = get_db()
    error = None

    try:
        if not email:
            error = "Email is required."
        elif not password:
            error = "Password is required."

        if error is None:
            db.execute(
                "INSERT INTO rt_users (email, password) VALUES (?, ?)",
                (email, generate_password_hash(password)),
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
@bp.output({}, 200)
@auth.verify_password
@bp.doc(
    summary="Login a user",
    description="Login a user with a username and password.",
)
def login(data):
    email = data["email"]
    password = data["password"]

    db = get_db()
    error = None

    try:
        if not email:
            error = "Email is required."
        elif not password:
            error = "Password is required."

        if error is None:
            user_requested = db.execute(
                "SELECT id, name, email FROM rt_users WHERE username = ?", (email,)
            ).fetchone()

            if user_requested is None or not check_password_hash(
                user_requested["password"], password
            ):
                abort(401, "Incorrect username or password.")
            else:
                session["user"] = user_requested

                # return a 200 status code on successful login
                return jsonify({}), 200
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
def user():
    return UserResponse().dump(auth.current_user)
