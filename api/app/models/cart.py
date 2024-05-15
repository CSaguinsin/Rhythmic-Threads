from datetime import datetime

from apiflask import Schema, fields

from app.models.product import Product


class CartItemSchema(Schema):
    id = fields.Integer(dump_only=True)
    cart_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    qty = fields.Integer(required=False, dump_default=1)
    size = fields.String(required=True)
    date_added = fields.DateTime(dump_only=True, dump_default=datetime.now()).format


class CartSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)
    created = fields.DateTime(dump_only=True, dump_default=datetime.now()).format
    updated = fields.DateTime(dump_only=True, dump_default=datetime.now()).format


# Schema for cart creation
class CartInitSchema(CartSchema):
    exclude = ["cart_items", "created", "updated"]


class CartRequest(Schema):
    id = fields.Integer(dump_only=True)
    qty = fields.Integer(required=False, dump_default=1)
    size = fields.String(required=True)
    product = fields.Nested(Product)
    date_added = fields.DateTime(dump_only=True).format


class CartItemRequest(Schema):
    user_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    qty = fields.Integer(required=False, dump_default=1)
    size = fields.String(required=True)
