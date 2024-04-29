from apiflask import Schema, fields
from datetime import datetime


class User(Schema):
    uid = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    name = fields.String(required=True)
    created = fields.DateTime(dump_only=True, dump_default=datetime.now())
    updated = fields.DateTime(dump_only=True, dump_default=datetime.now())


# request input structure for @bp.input
class UserRequest(Schema):
    username = fields.String()
    password = fields.String()
    name = fields.String()


# response output structure for @bp.output
class UserResponse(Schema):
    uid = fields.Integer()
    username = fields.String()
    name = fields.String()
    created = fields.DateTime()
    updated = fields.DateTime()
