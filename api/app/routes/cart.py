from apiflask import APIBlueprint, abort
from flask import jsonify
from flask_jwt_extended import jwt_required, current_user
from marshmallow import ValidationError
from marshmallow.fields import Integer

from app.db import get_db, close_db
from app.models.generic import GenericResponse
from app.models.cart import CartRequest, CartItemRequest, CartSchema
from app.routes import auth_token

bp = APIBlueprint("cart", __name__, url_prefix="/cart")


@bp.get("")
@bp.output(CartRequest(many=True))
@bp.auth_required(auth_token)
@jwt_required()
@bp.doc(summary="Get the user's shopping cart items")
def get_cart():
    db = get_db()

    try:
        # get current user's id
        user_id = current_user["id"]

        # get the user's shopping cart items and from cart_items and products table
        user_cart = db.execute(
            """
            SELECT
                rt_cart_items.id,
                rt_cart_items.qty,
                rt_cart_items.size,
                rt_cart_items.date_added,
                rt_products.image_url,
                rt_products.name,
                rt_products.description,
                rt_products.collection,
                rt_products.category,
                rt_products.price,
                rt_products.ratings
            FROM rt_cart_items
            LEFT JOIN rt_products ON rt_cart_items.product_id = rt_products.id
            WHERE rt_cart_items.cart_id = (
                SELECT id FROM rt_carts WHERE user_id = ?
            )
            """,
            (user_id,),
        ).fetchall()

        # Transform the flat structure into a nested one
        parsed_user_cart = []

        for item in user_cart:
            parsed_item = {
                "id": item["id"],
                "qty": item["qty"],
                "size": item["size"],
                "date_added": item["date_added"],
                "product": {
                    "image_url": item["image_url"],
                    "name": item["name"],
                    "description": item["description"],
                    "collection": item["collection"],
                    "category": item["category"],
                    "size": item["size"],
                    "price": item["price"],
                    "ratings": item["ratings"],
                },
            }
            parsed_user_cart.append(parsed_item)

        return CartRequest(many=True).dump(parsed_user_cart)

    except Exception as e:
        abort(
            500,
            message="An error occurred while fetching the user's shopping cart items",
            detail=str(e),
        )


@bp.post("")
@bp.input(CartItemRequest, location="json")
@bp.output(GenericResponse, 201)
@bp.auth_required(auth_token)
@jwt_required()
@bp.doc(
    summary="Add or update an item to the user's shopping cart",
    description="Add product to the user's shopping cart, update "
    "the quantity if the product is already added.\n\n"
    "This requires a logged-in user to get the current user id.",
)
def add_to_cart(json_data):
    db = get_db()
    user_id = current_user["id"]

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
            # check if cart exists for the current user,, create if none
            cart_id = db.execute(
                "SELECT id FROM rt_carts WHERE user_id = ?", (user_id,)
            ).fetchone()[0]

            if cart_id is None:
                # create a new cart for the user, if not found
                db.execute("INSERT INTO rt_carts (user_id) VALUES (?)", (user_id,))
                db.commit()

            # check if the product is already added
            existing_product = db.execute(
                "SELECT * FROM rt_cart_items WHERE product_id = ? AND cart_id = ?",
                (
                    json_data["product_id"],
                    cart_id,
                ),
            ).fetchone()

            # if the product is already added, update the quantity
            if existing_product:
                new_qty = int(existing_product["qty"]) + int(json_data["qty"])
                db.execute(
                    "UPDATE rt_cart_items SET qty = ? WHERE product_id = ? AND cart_id = ? AND size = ?",
                    (
                        new_qty,
                        json_data["product_id"],
                        cart_id,
                        json_data["size"],
                    ),
                )
            else:
                # if the product is not added, add the product to the cart
                db.execute(
                    "INSERT INTO rt_cart_items (cart_id, product_id, qty, size) VALUES (?, ?, ?, ?)",
                    (
                        cart_id,
                        json_data["product_id"],
                        json_data["qty"],
                        json_data["size"],
                    ),
                )

            db.commit()
            return GenericResponse().dump({"message": "Item added to cart"}), 201

    except Exception as e:
        abort(
            500,
            message="An error occurred while adding the item to the user's shopping cart",
            detail=str(e),
        )

    finally:
        close_db()


@bp.delete("")
@bp.input({"product_id": Integer()}, location="query")
@bp.auth_required(auth_token)
@jwt_required()
@bp.doc(
    summary="Remove an item from the user's shopping cart",
    description="Remove a product from the user's shopping cart by providing the product id.",
)
def remove_from_cart(query_data):
    db = get_db()

    try:
        product_id = query_data["pid"]
        user_id = current_user["id"]

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
        return 200

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
