from apiflask import Schema, fields


class GenericResponse(Schema):
    message = fields.String()
