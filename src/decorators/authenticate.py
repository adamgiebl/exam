from bottle import request, response
from src.utils import Fore, decode_jwt, ppprint


def authenticate(allow_anonymous=False):
  def decorator(func):
    def inner(*args, **kwargs):
      try:
        decoded = decode_jwt(request.get_cookie("jwt"))
        request.user = decoded
        ppprint(f"User: { decoded['first_name'] } { decoded['last_name'] }, { decoded['email'] }, { decoded['hex_color'] }", Fore.CYAN)
        ppprint('Authenticated', Fore.GREEN)
      except Exception as e:
        request.user = None
        ppprint('Not Authenticated', Fore.RED)
        if (not allow_anonymous):
          response.status = 401
          return "Unauthorized"
        

      return func(*args, **kwargs)
    return inner
  return decorator
