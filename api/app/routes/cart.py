from apiflask import APIBlueprint, abort
from flask import jsonify
from marshmallow import ValidationError
from marshmallow.fields import Integer

from app.db import get_db, close_db
from app.models.cart import CartRequest, CartItemRequest

bp = APIBlueprint("cart", __name__, url_prefix="/cart")


@bp.get("")
@bp.input({"user_id": Integer()}, location="query")
@bp.output(CartRequest(many=True))
@bp.doc(summary="Get the user's shopping cart items")
def get_cart(query_data):
    db = get_db()

    try:
        # get current user's id
        user_id = query_data["user_id"]

        # get the user's shopping cart items and join with the cart items table
        cart = db.execute(
            "SELECT cart.id, cart.user_id, cart_item.* "
            "FROM rt_carts cart JOIN rt_cart_items cart_item ON cart.cart_items = cart_item.id "
            "WHERE cart.user_id = ?",
            (user_id,),
        ).fetchall()
        return CartRequest().dump(cart)

    except Exception as e:
        abort(
            500,
            message="An error occurred while fetching the user's shopping cart items",
            detail=str(e),
        )

    finally:
        db.close()


@bp.post("")
@bp.input({"user_id": Integer()}, location="query")
@bp.input(CartItemRequest, location="json")
@bp.doc(summary="Add or update an item to the user's shopping cart",
        description="Add product to the user's shopping cart, update "
                    "the quantity if the product is already added.\n\n"
                    "This requires a logged-in user to get the current user id.")
def add_to_cart(query_data, json_data):
    db = get_db()
    user_id = query_data["user_id"]

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
                "SELECT id FROM rt_carts WHERE user_id = ?", (user_id,)
            ).fetchone()

            if not cart_id:
                # create a new cart for the user, if not found
                db.execute("INSERT INTO rt_carts (user_id) VALUES (?)", (user_id,))

                # check if the product is already added
                existing_product = db.execute(
                    "SELECT qty FROM rt_cart_items WHERE product_id = ? AND cart_id = ?",
                    (json_data["product_id"],),
                    (json_data["cart_id"],),
                ).fetchone()

                # if the product is already added, update the quantity
                if existing_product:
                    db.execute(
                        "UPDATE rt_cart_items SET qty = ? WHERE product_id = ? AND cart_id = ?",
                        (existing_product["qty"] + json_data["qty"], json_data["product_id"], cart_id),
                    )
                else:
                    # if the product is not added, add the product to the cart
                    db.execute(
                        "INSERT INTO rt_cart_items (product_id, qty) VALUES (?, ?)",
                        (cart_id, json_data["product_id"], json_data["qty"]),
                    )

            db.commit()

    except Exception as e:
        abort(
            500,
            message="An error occurred while adding the item to the user's shopping cart",
            detail=str(e),
        )

    finally:
        close_db()


@bp.delete("")
@bp.input({"user_id": Integer(), "product_id": Integer()}, location="query")
@bp.doc(summary="Remove an item from the user's shopping cart",
        description="Remove a product from the user's shopping cart by providing the product id.")
def remove_from_cart(query_data):
    db = get_db()

    try:
        product_id = query_data["pid"]
        user_id = query_data["user_id"]

        # get the cart for the current user
        cart_id = db.execute(
            "SELECT id FROM rt_carts WHERE user_id = ?", (user_id,)
        ).fetchone()

        # remove the product from the cart
        db.execute(
            "DELETE FROM rt_cart_items WHERE cart_id = ? AND product_id = ?",
            (cart_id, product_id),
        )
        db.commit()

    except Exception as e:
        abort(
            500,
            message="An error occurred while removing the item from the user's shopping cart",
            detail=str(e),
        )

    finally:
        close_db()


def __validate_cart(cart):
    """
    Validate the input cart item

    :param cart: CartRequest
    :return: str
    """

    try:
        CartItemRequest().load(cart)
        return None
    except ValidationError as e:
        return jsonify(e.messages)
