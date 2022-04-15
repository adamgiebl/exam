from bottle import get, request, response, view
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate
from src.decorators.is_fetch import is_fetch


@get("/posts")
@view("posts")
@authenticate()
@is_fetch()
def _():
  db = DBInterface()

  query = """SELECT post.id, post.text, post.created_at, user.last_name ,user.first_name, user.hex_color
  FROM posts post
  JOIN users user WHERE user.id = post.user_id AND user.id = ?
  ORDER BY post.created_at DESC"""

  posts = db.fetch_all(query, (request.user["id"],))

  if (db.exception):
    response.status = 500
    return 'Something went wrong'

  return dict(posts=posts, user=request.user, is_fetch=request.is_fetch)
