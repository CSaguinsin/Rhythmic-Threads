import decimal
from datetime import datetime

from apiflask import Schema, fields


class Product(Schema):
    id = fields.Integer(dump_only=True)
    image_url = fields.String(required=True, dump_default="/imgs/na.jpg")
    name = fields.String(required=True)
    description = fields.String(required=True)
    collection = fields.String(required=True, allow_none=True) # T-shirt, jacket, shorts
    category = fields.String(required=True) # Male, female, kids
    size = fields.String(required=True) # S, M, L, XL, XXL
    price = fields.Decimal(required=True, rounding=decimal.ROUND_FLOOR, as_string=True) # 10.00 (two decimal places)
    ratings = fields.Integer(allow_none=True)
    created = fields.DateTime(dump_only=True, dump_default=datetime.now()).format
    updated = fields.DateTime(dump_only=True, dump_default=datetime.now()).format
