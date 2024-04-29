import decimal
from datetime import datetime

from apiflask import Schema, fields


class Product(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    collection = fields.String(required=True, allow_none=True)
    category = fields.String(required=True)
    sx = fields.String(required=True)
    size = fields.String(required=True)
    price = fields.Decimal(required=True, rounding=decimal.ROUND_FLOOR)
    ratings = fields.Integer(allow_none=True)
    created = fields.DateTime(dump_only=True, dump_default=datetime.now()).format
    updated = fields.DateTime(dump_only=True, dump_default=datetime.now()).format


class ProductRequest(Product):
    exclude = ["id", "created", "updated"]


class ProductResponse(Product):
    exclude = ["updated"]
