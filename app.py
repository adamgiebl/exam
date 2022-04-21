from functools import wraps

from bottle import default_app, error, request, run, view

import src.routes.files.image_POST
import src.routes.following.followers_GET
import src.routes.following.following_GET
import src.routes.following.following_POST
import src.routes.home.home_GET
import src.routes.login.login_GET
import src.routes.login.login_POST
import src.routes.login.logout_POST
import src.routes.posts.posts_DELETE
import src.routes.posts.posts_POST
import src.routes.profile.profile_GET
import src.routes.signup.signup_GET
import src.routes.signup.signup_POST
import src.routes.static
import src.routes.users.users_GET
from src.decorators.is_fetch import is_fetch


@error(404)
@view("404")
@is_fetch()
def _(error):
  return dict(error=error, is_fetch=request.is_fetch)

try:
  import production
  application = default_app()
except Exception as ex:
  run(host="localhost", port=3333, debug=True, reloader=True)
