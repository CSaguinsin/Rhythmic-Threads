from datetime import datetime

from apiflask import Schema, fields


class User(Schema):
    uid = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    name = fields.String(required=True)
    created = fields.DateTime(dump_only=True, dump_default=datetime.now()).format
    updated = fields.DateTime(dump_only=True, dump_default=datetime.now()).format


# request input structure for @bp.input
class UserRequest(User):
    exclude = ["uid", "created", "updated"]


# response output structure for @bp.output
class UserResponse(User):
    exclude = ["updated"]
