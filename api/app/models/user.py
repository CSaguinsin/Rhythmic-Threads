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
class UserRequest(Schema):
    username = fields.Email(required=True)
    password = fields.String(required=True)
    name = fields.String(required=False, allow_none=True)


class UserLoginRequest(Schema):
    username = fields.Email(required=True)
    password = fields.String(required=True)


# response output structure for @bp.output
class UserResponse(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.Email(required=True)
    name = fields.String(required=False, allow_none=True)
    created = fields.DateTime(dump_only=True, dump_default=datetime.now()).format
