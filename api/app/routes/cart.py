from apiflask import APIBlueprint, abort, HTTPBasicAuth
from flask import jsonify, session
from marshmallow import ValidationError
from marshmallow.fields import Integer

from app.db import get_db
from app.models.cart import CartRequest, CartItemRequest

bp = APIBlueprint("cart", __name__, url_prefix="/cart")
auth = HTTPBasicAuth()


@bp.get("")
@bp.output(CartRequest(many=True))
@bp.auth_required(auth)
@bp.doc(summary="Get the user's shopping cart items")
def get_cart():
    db = get_db()

    try:
        # get current user's id
        user_id = session.get("user")["id"]

        # get the user's shopping cart items and join with the cart items table
        cart = db.execute(
            "SELECT cart.id, cart.user_id, cart_item.* "
            "FROM rt_carts cart JOIN rt_cart_item cart_item ON cart.cart_items = cart_item.id "
            "WHERE cart.user_id = ?",
            (user_id,),
        ).fetchall()
        return CartRequest().dump(cart)

    except Exception as e:
        abort(
            500,
            message="An error occurred while fetching the user's shopping cart items",
            detail=e,
        )

    finally:
        db.close()


@bp.post("")
@bp.input(CartItemRequest, location="json")
@bp.auth_required(auth)
@bp.doc(summary="Add or update an item to the user's shopping cart",
        description="Add product to the user's shopping cart, update "
                    "the quantity if the product is already added.\n\n"
                    "This requires a logged-in user to get the current user id.")
def add_to_cart(json_data):
    db = get_db()

    try:
        error = __validate_cart(json_data)

        if error:
            # Throw 400 if input doesn't match the schema/types.
            abort(
                400,
                message="Input does not match the expected schema or types",
                detail=error,
            )
        else:
            # check if cart exists for the current user, get cart ID
            cart_id = db.execute(
                "SELECT id FROM rt_carts WHERE user_id = ?", (session.get("user_id"),)
            ).fetchone()

            if not cart_id:
                # create a new cart for the user, if not found
                db.execute("INSERT INTO rt_carts (user_id) VALUES (?)", (session.get("user_id"),))

                # check if the product is already added
                existing_product = db.execute(
                    "SELECT qty FROM rt_cart_item WHERE product_id = ? AND cart_id = ?",
                    (json_data["product_id"],),
                    (json_data["cart_id"],),
                ).fetchone()

                # if the product is already added, update the quantity
                if existing_product:
                    db.execute(
                        "UPDATE rt_cart_item SET qty = ? WHERE product_id = ? AND cart_id = ?",
                        (existing_product["qty"] + json_data["qty"], json_data["product_id"], cart_id),
                    )
                else:
                    # if the product is not added, add the product to the cart
                    db.execute(
                        "INSERT INTO rt_cart_item (product_id, qty) VALUES (?, ?, ?)",
                        (cart_id, json_data["product_id"], json_data["qty"]),
                    )

            db.commit()

    except Exception as e:
        abort(
            500,
            message="An error occurred while adding the item to the user's shopping cart",
            detail=e,
        )

    finally:
        db.close()


@bp.delete("")
@bp.input({"product_id": Integer()}, location="query")
@bp.auth_required(auth)
@bp.doc(summary="Remove an item from the user's shopping cart",
        description="Remove a product from the user's shopping cart by providing the product id.")
def remove_from_cart(query_data):
    db = get_db()

    try:
        user_id = session.get("user")["id"]
        product_id = query_data["pid"]

        # get the cart for the current user
        cart_id = db.execute(
            "SELECT id FROM rt_carts WHERE user_id = ?", (user_id,)
        ).fetchone()

        # remove the product from the cart
        db.execute(
            "DELETE FROM rt_cart_item WHERE cart_id = ? AND product_id = ?",
            (cart_id, product_id),
        )
        db.commit()

    except Exception as e:
        abort(
            500,
            message="An error occurred while removing the item from the user's shopping cart",
            detail=e,
        )

    finally:
        db.close()


def __validate_cart(cart):
    """
    Validate the input cart item

    :param cart: CartRequest
    :return: str
    """

    try:
        CartRequest().load(cart)
        return None
    except ValidationError as e:
        return jsonify(e.messages)
