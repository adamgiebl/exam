from wsgiref import validate

from marshmallow import Schema, fields, validate


class PostSchema(Schema):
    text = fields.String(required=True, validate=validate.Length(min=1, max=100))
