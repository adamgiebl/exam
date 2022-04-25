from marshmallow import Schema, fields, validate


class SignupUserSchema(Schema):
  email = fields.Email(required=True)
  username = fields.String(required=True, validate=validate.Length(min=1, max=50))
  first_name = fields.String(required=True, validate=validate.Length(min=1, max=50))
  last_name = fields.String(required=True, validate=validate.Length(min=1, max=50))
  password = fields.String(required=True, validate=validate.Length(min=1, max=50))
  bio = fields.String(required=False)
