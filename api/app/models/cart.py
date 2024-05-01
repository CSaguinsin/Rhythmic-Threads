from datetime import datetime

from apiflask import Schema, fields


class CartItemSchema(Schema):
    id = fields.Integer(dump_only=True)
    cart_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    qty = fields.Integer(required=False, dump_default=1)
    added_in = fields.DateTime(dump_only=True, dump_default=datetime.now()).format


class CartSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)
    cart_items = fields.Nested(CartItemSchema(), many=True)
    created = fields.DateTime(dump_only=True, dump_default=datetime.now()).format
    updated = fields.DateTime(dump_only=True, dump_default=datetime.now()).format


# Schema for cart creation
class CartInitSchema(CartSchema):
    exclude = ["cart_items", "created", "updated"]


class CartRequest(CartSchema):
    exclude = ["created", "updated"]


class CartItemRequest(CartItemSchema):
    exclude = ["cart_id"]
