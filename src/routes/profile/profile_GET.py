from urllib import response

from bottle import get, request, view
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate
from src.decorators.is_fetch import is_fetch


@get("/profile/<username>")
@view("profile")
@authenticate(allow_anonymous=True)
@is_fetch()
def _(username):
  db = DBInterface()

  query_user_posts = """SELECT post.text, post.created_at, user.last_name, user.username, user.first_name, user.hex_color
  FROM posts post
  JOIN users user WHERE user.id = post.user_id AND user.username = ?
  ORDER BY post.created_at DESC
  """

  query_user_by_id = "SELECT * FROM users user WHERE user.username = ?"

  posts = db.fetch_all(query_user_posts, (username, ), close_connection=False)

  person = db.fetch_one(query_user_by_id, (username, ), close_connection=False)

  query_users = "SELECT * FROM users"

  users = db.fetch_all(query_users)

  print(posts)
  print(person)

  if (db.exception):
    print(db.exception)
    response.status = 500
    return "Something went wrong"
  
  if (bool(request.user)):
    return dict(posts=posts, user=request.user, people=users, person=person, is_fetch=request.is_fetch)
  else:
    return dict(posts=posts, person=person, people=users, is_fetch=request.is_fetch)
