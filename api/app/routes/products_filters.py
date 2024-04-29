from decimal import Decimal

from apiflask import APIBlueprint, abort, HTTPBasicAuth
from app.db import get_db, close_db

from ..models.product import ProductResponse

bp = APIBlueprint("products filters", __name__, url_prefix="/products/filter")
auth = HTTPBasicAuth()


@bp.get("/new")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products created in 7 days")
def get_new_arrivals():
    try:
        db = get_db()
        products = db.execute(
            "SELECT id, name, description, collection, category, sx, size, price, ratings, created "
            "FROM products WHERE created >= datetime('now', '-7 days')"
        ).fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/ratings/<int:rating>")
@bp.input({"rating": int}, location="query")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products with a specific rating",
        description="Ratings are comprised of 1 -> 5 as integers, 1 being the lowest, 5 the highest.")
def get_products_by_rating(ratings):
    try:
        if ratings < 1 or ratings > 5:
            abort(
                status_code=422,
                message="Ratings must be between 1 and 5",
            )
        else:
            db = get_db()
            products = db.execute(
                "SELECT id, name, description, collection, category, sx, size, price, ratings, created "
                "FROM products WHERE ratings = ?", (ratings,)
            ).fetchall()
            return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/category/<string:category>")
@bp.input({"category": str}, location="query")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products in a specific category")
def get_products_by_category(category):
    try:
        db = get_db()
        products = db.execute(
            "SELECT id, name, description, collection, category, sx, size, price, ratings, created "
            "FROM products WHERE category = ?", (category,)
        ).fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/collection/<string:collection>")
@bp.input({"collection": str}, location="query")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products in a specific collection")
def get_products_by_collection(collection):
    try:
        db = get_db()
        products = db.execute(
            "SELECT id, name, description, collection, category, sx, size, price, ratings, created "
            "FROM products WHERE collection = ?", (collection,)
        ).fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/sx/<string:sx>")
@bp.input({"sx": str}, location="query")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products within a specific sex", description="Sexes are 'M', 'F', 'U' for unisex.")
def get_products_by_sx(sx):
    try:
        db = get_db()
        products = db.execute("SELECT id, name, description, collection, category, sx, size, price, ratings, created "
                              "FROM products WHERE sx = ?", (sx,)).fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/size/<string:size>")
@bp.input({"size": str}, location="query")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products with a specific size",
        description="Sizes are in the format of 'S', 'M', 'L', 'XL', etc.")
def get_products_by_size(size):
    try:
        db = get_db()
        products = db.execute(
            "SELECT id, name, description, collection, category, sx, size, price, ratings, created "
            "FROM products WHERE size = ?", (size,)
        ).fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/price/<float:starting_price>-<float:ending_price>")
@bp.input({"starting_price": Decimal, "ending_price": Decimal}, location="query")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products within a specific price range")
def get_products_by_price_range(starting_price, ending_price):
    try:
        if starting_price >= ending_price:
            abort(
                status_code=422,
                message="Starting price cannot be greater than or equal the ending price",
            )
        else:
            db = get_db()
            products = db.execute(
                "SELECT id, name, description, collection, category, sx, size, price, ratings, created "
                "FROM products WHERE price BETWEEN ? AND ?",
                (starting_price, ending_price),
            ).fetchall()
            return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()
