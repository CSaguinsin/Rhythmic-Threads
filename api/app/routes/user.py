from apiflask import APIBlueprint, abort
from marshmallow.fields import String
from werkzeug.security import generate_password_hash

from app.db import get_db, close_db
from app.models.user import UserRequest, UserResponse

bp = APIBlueprint("user", __name__, url_prefix="/user")


@bp.get("/<int:id>")
@bp.output(UserResponse, 200)
@bp.doc(summary="Get user by id")
def get_user_by_id(id):
    db = get_db()

    try:
        user = db.execute(
            "SELECT id, username, name, created FROM rt_users WHERE id = ?", (id,)
        ).fetchone()

        if user is not None:
            return UserResponse().dump(user)
        else:
            abort(404, f"User {id} not found.")

    except Exception as e:
        abort(
            500,
            message="An error occurred while fetching the user's information",
            detail=str(e),
        )
    finally:
        close_db()


@bp.post("/<int:id>")
@bp.input(UserRequest, location="json")
@bp.output({"message": String()}, 200)
@bp.doc(summary="Update user email and name")
def update_user(id, json_data):
    db = get_db()

    try:
        # update name
        if "name" in json_data:
            db.execute(
                "UPDATE rt_users SET name = ? WHERE id = ?", (json_data["name"], id)
            )
        if "username" in json_data:
            db.execute(
                "UPDATE rt_users SET username = ? WHERE id = ?", (json_data["username"], id)
            )
        db.commit()
        return {"message": f"User {id} successfully updated."}, 200

    except Exception as e:
        abort(
            500,
            message="An error occurred while updating the user's information",
            detail=str(e),
        )
    finally:
        close_db()


@bp.delete("/<int:id>")
@bp.output({"message": String()}, 200)
@bp.doc(summary="Delete user by id")
def delete_user(id):
    db = get_db()

    try:
        db.execute("DELETE FROM rt_users WHERE id = ?", (id,))
        db.commit()
        return {"message": f"User {id} successfully deleted."}, 200

    except Exception as e:
        abort(
            500,
            message="An error occurred while deleting the user",
            detail=str(e),
        )
    finally:
        close_db()


@bp.post("/<int:id>/pw")
@bp.input({"password": String()}, location="json")
@bp.output({"message": String()}, 200)
@bp.doc(summary="Update user password")
def update_user_password(id, json_data):
    db = get_db()

    try:
        db.execute(
            "UPDATE rt_users SET password = ? WHERE id = ?",
            (generate_password_hash(json_data["password"]), id),
        )
        db.commit()
        return {"message": f"User {id} password successfully updated."}, 200

    except Exception as e:
        abort(
            500,
            message="An error occurred while updating the user's password",
            detail=str(e),
        )

    finally:
        close_db()
