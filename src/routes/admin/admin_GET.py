
from bottle import get, request, view
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate
from src.decorators.is_fetch import is_fetch


@get("/admin")
@view("admin")
@authenticate()
@is_fetch()
def _():

  db = DBInterface()

  query = "SELECT * FROM users"

  query_user_posts = """SELECT post.id, post.text, post.created_at, user.last_name, user.image, user.username, user.first_name, user.hex_color, user.image
  FROM posts post
  JOIN users user WHERE user.id = post.user_id
  ORDER BY post.created_at DESC
  """

  users = db.fetch_all(query, close_connection=False)

  posts = db.fetch_all(query_user_posts)

  return dict(users=users, user=request.user, is_fetch=request.is_fetch, posts=posts)
