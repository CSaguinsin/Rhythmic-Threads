from apiflask import APIBlueprint, HTTPBasicAuth

from app.db import get_db, close_db
from ..models.product import ProductResponse

bp = APIBlueprint("products", __name__, url_prefix="/products")
auth = HTTPBasicAuth()


@bp.get("/")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products")
def get_products():
    try:
        db = get_db()
        products = db.execute("SELECT * FROM product").fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/new-arrivals")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products created in 7 days")
def get_new_arrivals():
    try:
        db = get_db()
        products = db.execute(
            "SELECT * FROM product WHERE created >= datetime('now', '-7 days')"
        ).fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/<int:ratings>")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products with a specific rating")
def get_products_by_rating(ratings):
    try:
        db = get_db()
        products = db.execute(
            "SELECT * FROM product WHERE ratings = ?", (ratings,)
        ).fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/<string:category>")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products in a specific category")
def get_products_by_category(category):
    try:
        db = get_db()
        products = db.execute(
            "SELECT * FROM product WHERE category = ?", (category,)
        ).fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/<string:sx>")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products within a specific sex")
def get_products_by_sx(sx):
    try:
        db = get_db()
        products = db.execute("SELECT * FROM product WHERE sx = ?", (sx,)).fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/<string:size>")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products with a specific size")
def get_products_by_size(size):
    try:
        db = get_db()
        products = db.execute(
            "SELECT * FROM product WHERE size = ?", (size,)
        ).fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()


@bp.get("/<int:starting_price>-<int:ending_price>")
@bp.output(ProductResponse(many=True))
@bp.doc(summary="Get all products within a specific price range")
def get_products_by_price_range(starting_price, ending_price):
    try:
        db = get_db()
        products = db.execute(
            "SELECT * FROM product WHERE price BETWEEN ? AND ?",
            (starting_price, ending_price),
        ).fetchall()
        return ProductResponse().dump(products)
    except Exception as e:
        return str(e.__cause__)
    finally:
        close_db()
