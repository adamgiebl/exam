from bottle import default_app, post, run

import src.routes.home.home_GET
import src.routes.posts.posts_GET
import src.routes.posts.posts_POST
import src.routes.static
from src.decorators.validate import validate
from src.schemas.user import UserSchema


@post("/test")
@validate(UserSchema)
def _():
  return "yo"

try:
  import production
  application = default_app()
except Exception as ex:
  print("Server running on development")
  run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
