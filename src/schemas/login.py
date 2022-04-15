from marshmallow import Schema, fields, validate


class LoginUserSchema(Schema):
  email = fields.Email(required=True)
  password = fields.String(required=True, validate=validate.Length(min=1, max=50))
