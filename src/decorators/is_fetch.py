from bottle import request


def is_fetch():
  def decorator(func):
    def inner(*args, **kwargs):
      request.is_fetch = True if request.headers.get('From-Fetch') else False 
      return func(*args, **kwargs)
    return inner
  return decorator
