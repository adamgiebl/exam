from pprint import pprint

from bottle import request, response
from marshmallow import ValidationError


def validate(Schema):
  def decorator(func):
    def inner(*args, **kwargs):
      schema = Schema()
      pprint("Here:")
      pprint(request.json)
      try:
        result = schema.load(request.json)
      except ValidationError as err:
        pprint(err.messages)
        response.status = 400
        return err.messages
      return func(*args, **kwargs)
    return inner
  return decorator
