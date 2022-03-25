from marshmallow import Schema, fields

class UserSchema(Schema):
    age = fields.Integer(required=True)
    gender = fields.String(required=True)