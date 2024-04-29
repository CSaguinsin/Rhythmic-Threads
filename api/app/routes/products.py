from apiflask import APIBlueprint, abort, HTTPBasicAuth
from app.db import get_db, close_db
from flask import jsonify
from marshmallow import ValidationError

from ..models.product import ProductResponse, ProductRequest

bp = APIBlueprint("products", __name__, url_prefix="/products")
auth = HTTPBasicAuth()


@bp.get("/")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products")
def get_products():
    try:
        db = get_db()
        products = db.execute("SELECT id, name, description, collection, category, sx, size, price, ratings, created "
                              "FROM products").fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/<int:id>")
@bp.output(ProductResponse)
@bp.doc(summary="Get a product by ID")
def get_product_by_id(pid):
    try:
        db = get_db()
        product = db.execute("SELECT id, name, description, collection, category, sx, size, price, ratings, created "
                             "FROM products WHERE id = ?", (pid,)).fetchone()
        return ProductResponse().dump(product)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.post("/")
@bp.input(ProductRequest, location="json")
@bp.output(ProductResponse, 201)
@bp.doc(summary="Create a new product")
def create_product(product):
    error = __validate_product(product)
    db = get_db()

    try:
        if error:
            abort(
                status_code=400,
                message="Validation Error",
                detail=error
            )

        if error is None:
            db.execute(
                "INSERT INTO product (name, description, collection, category, sx, size, price, ratings) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    product["name"],
                    product["description"],
                    product["collection"],
                    product["category"],
                    product["sx"],
                    product["size"],
                    product["price"],
                    product["ratings"],
                ),
            )
            db.commit()

            # Get the product that was just created
            product = db.execute("SELECT * FROM products WHERE name = ?", (product["name"],)).fetchone()
            return ProductResponse().dump(product)
    except Exception as e:
        abort(500, str(e.__cause__))
    finally:
        close_db()


@bp.patch("/<int:id>")
@bp.input(ProductRequest, location="json")
@bp.output(ProductResponse)
@bp.doc(summary="Update a product by ID")
def update_product(pid, product):
    error = __validate_product(product)
    db = get_db()

    try:
        if error:
            abort(
                status_code=400,
                message="Validation Error",
                detail=error
            )

        if error is None:
            db.execute(
                "UPDATE products SET name = ?, description = ?, collection = ?, category = ?, sx = ?, size = ?, "
                "price = ?, ratings = ?"
                "WHERE id = ?",
                (
                    product["name"],
                    product["description"],
                    product["collection"],
                    product["category"],
                    product["sx"],
                    product["size"],
                    product["price"],
                    product["ratings"],
                    pid,
                ),
            )
            db.commit()

            # Get the updated product
            product = db.execute(
                "SELECT id, name, description, collection, category, sx, size, price, ratings, created "
                "FROM products WHERE id = ?", (pid,)).fetchone()
            return ProductResponse().dump(product)

    except Exception as e:
        abort(500, str(e.__cause__))
    finally:
        close_db()


def __validate_product(product):
    """
    Validate if input fields are correct using marshmallow.

    :param product:
    :return:
    """

    try:
        ProductRequest().load(product)
        return None
    except ValidationError as e:
        return jsonify(e.messages)
