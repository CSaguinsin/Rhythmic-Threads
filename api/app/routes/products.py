from apiflask import APIBlueprint, abort
from apiflask.fields import Integer, String
from flask import jsonify
from marshmallow import ValidationError

from app.db import get_db, close_db
from app.models.product import ProductResponse, ProductRequest

bp = APIBlueprint("products", __name__, url_prefix="/products")


@bp.get("")
@bp.input({"ratings": Integer(), "category": String(), "collection": String(), "price": String()}, location="query")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products",
        description="You can filter products based on provided name parameters.\n\n"
                    "Ex. /products?ratings=4&category=Clothing&collection=Summer 2023&price=100-200")
def get_products(query_data):
    """
    Get products based on the named parameters provided in the URL.

    :param query_data:
    :return: Returns all products by default
    """

    db = get_db()
    query = "SELECT id, name, description, collection, category, sx, size, price, ratings, created FROM rt_products"
    params = []

    if query_data:
        query += " WHERE "
        if "ratings" in query_data:
            query += "ratings = ? AND "
            params.append(query_data["ratings"])
        if "category" in query_data:
            query += "category = ? AND "
            params.append(query_data["category"])
        if "collection" in query_data:
            query += "collection = ? AND "
            params.append(query_data["collection"])
        if "price" in query_data:
            price = query_data["price"].split("-")
            query += "price BETWEEN ? AND ? AND "

            # set min price to 0 if no min price is provided
            try:
                params.append(price[0])
            except IndexError:
                params.append(0)

            # set max price to 9999999 if no max price is provided
            try:
                params.append(price[1])
            except IndexError:
                params.append(9999999)

        query = query[:-5]

    try:
        products = db.execute(query, params).fetchall()
        return ProductResponse(many=True).dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/<int:pid>")
@bp.output(ProductResponse)
@bp.doc(summary="Get a product by ID")
def get_product_by_id(pid):
    try:
        db = get_db()
        product = db.execute("SELECT id, name, description, collection, category, sx, size, price, ratings, created "
                             "FROM rt_products WHERE id = ?", (pid,)).fetchone()

        if product is not None:
            return ProductResponse().dump(product)
        else:
            return jsonify({"message": f"Product {pid} not found."})
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.post("")
@bp.input(ProductRequest, location="json")
@bp.output(ProductResponse, 201)
@bp.doc(summary="Create a new product")
def create_product(json_data):
    error = __validate_product(json_data)
    db = get_db()

    try:
        if error:
            return jsonify(
                {
                    "message": "Validation Error",
                    "detail": error
                }
            )

        if error is None:
            db.execute(
                "INSERT INTO rt_products (name, description, collection, category, sx, size, price, ratings) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    json_data["name"],
                    json_data["description"],
                    json_data["collection"],
                    json_data["category"],
                    json_data["sx"],
                    json_data["size"],
                    str(json_data["price"]),
                    json_data["ratings"],
                ),
            )
            db.commit()

            # Get the product that was just created
            product = db.execute("SELECT * FROM rt_products WHERE name = ?", (json_data["name"],)).fetchone()
            return ProductResponse().dump(product)
    except Exception as e:
        abort(
            status_code=500,
            message=str("An error occurred while creating the product."),
            detail=(str(e))
        )
    finally:
        close_db()


@bp.patch("/<int:pid>")
@bp.input(ProductRequest, location="json")
@bp.output(ProductResponse)
@bp.doc(summary="Update a product by ID")
def update_product(pid, json_data):
    product = json_data

    error = __validate_product(product)
    db = get_db()

    try:
        if error:
            return jsonify(
                {
                    "message": "Validation Error",
                    "detail": error
                }
            )

        if error is None:
            db.execute(
                "UPDATE rt_products SET name = ?, description = ?, collection = ?, category = ?, sx = ?, size = ?, "
                "price = ?, ratings = ?"
                "WHERE id = ?",
                (
                    product["name"],
                    product["description"],
                    product["collection"],
                    product["category"],
                    product["sx"],
                    product["size"],
                    str(product["price"]),
                    product["ratings"],
                    pid,
                ),
            )
            db.commit()

            # Get the updated product
            product = db.execute(
                "SELECT id, name, description, collection, category, sx, size, price, ratings, created "
                "FROM rt_products WHERE id = ?", (pid,)).fetchone()
            return ProductResponse().dump(product)

    except Exception as e:
        abort(
            status_code=500,
            message=str("An error occurred while creating the product."),
            detail=(str(e))
        )
    finally:
        close_db()


@bp.delete("/<int:pid>")
@bp.output({"message": str}, 200)
def delete_product(pid):
    db = get_db()

    try:
        db.execute("DELETE FROM rt_products WHERE id = ?", (pid,))
        db.commit()
        return jsonify({"message": f"Product {pid} successfully deleted."})
    except Exception as e:
        return str(e.__cause__)
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
