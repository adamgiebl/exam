from bottle import get, request, response, view
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate
from src.decorators.is_fetch import is_fetch


@get("/followers")
@view("following")
@authenticate()
@is_fetch()
def _():
  db = DBInterface()

  query = """SELECT followers.followee_id, followers.follower_id, user.username, user.image, user.hex_color, user.first_name, user.last_name FROM users user
  JOIN followers WHERE followers.followee_id = ? AND followers.follower_id = user.id"""

  people = db.fetch_all(query, (request.user["id"],))

  if (db.exception):
    response.status = 500
    return 'Something went wrong'

  return dict(users=people, user=request.user, is_fetch=request.is_fetch, title="Your followers")
