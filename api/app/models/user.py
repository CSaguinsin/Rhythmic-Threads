from datetime import datetime

from apiflask import Schema, fields


class User(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.Email(required=True)
    password = fields.String(required=True)
    name = fields.String(required=False, allow_none=True)
    created = fields.DateTime(dump_only=True, dump_default=datetime.now()).format
    updated = fields.DateTime(dump_only=True, dump_default=datetime.now()).format


# request input structure for @bp.input
class UserRequest(User):
    exclude = ["id", "created", "updated"]


class UserLoginRequest(User):
    exclude = ["id", "name", "created", "updated"]

# response output structure for @bp.output
class UserResponse(User):
    exclude = ["password", "updated"]
