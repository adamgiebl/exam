from pprint import pprint

from bottle import request, response
from marshmallow import ValidationError


def validate(Schema):
  def decorator(func):
    def inner(*args, **kwargs):
      schema = Schema()
      if (bool(request.json)):
        source = request.json
      elif (bool(request.forms)):
        source = request.forms
      else:
        source = None
      try:
        request.validated_data = schema.load(source)
      except ValidationError as err:
        pprint(err.messages)
        response.status = 400
        return err.messages
      return func(*args, **kwargs)
    return inner
  return decorator
