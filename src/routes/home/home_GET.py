from urllib import response

from bottle import get, request, view
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate
from src.decorators.is_fetch import is_fetch


@get("/")
@view("index")
@authenticate(allow_anonymous=True)
@is_fetch()
def _():

  db = DBInterface()

  query_posts_users = """SELECT post.text, post.created_at, user.last_name ,user.first_name, user.hex_color
  FROM posts post
  JOIN users user WHERE user.id = post.user_id
  ORDER BY post.created_at DESC"""

  posts = db.fetch_all(query_posts_users, close_connection=False)

  query_users = "SELECT * FROM users WHERE users.id != ?"

  users = db.fetch_all(query_users, (request.user.get('id', None) if request.user else "None", ))

  if (db.exception):
    print(db.exception)
    response.status = 500
    return "Something went wrong"
  
  if (bool(request.user)):
    return dict(posts=posts, user=request.user, people=users, is_fetch=request.is_fetch)
  else:
    return dict(posts=posts, people=users, is_fetch=request.is_fetch)
 
