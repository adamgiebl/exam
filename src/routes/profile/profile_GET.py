from bottle import get, redirect, request, response, view
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate
from src.decorators.is_fetch import is_fetch
from src.utils import encode_jwt, without_keys


@get("/profile/<username>")
@view("profile")
@authenticate(allow_anonymous=True)
@is_fetch()
def _(username):
  db = DBInterface()

  user = request.user

  query_user_posts = """SELECT post.id, post.text, post.created_at, user.last_name, user.image, user.username, user.first_name, user.hex_color, user.image
  FROM posts post
  JOIN users user WHERE user.id = post.user_id AND user.username = ?
  ORDER BY post.created_at DESC
  """

  query_user_by_id = "SELECT * FROM users user WHERE user.username = ?"

  posts = db.fetch_all(query_user_posts, (username, ), close_connection=False)

  person = db.fetch_one(query_user_by_id, (username, ), close_connection=False)

  query_users = "SELECT * FROM users"

  reload = bool(request.query.get('reload-jwt', None))
  print("Should reload")
  print(reload)

  users = db.fetch_all(query_users, close_connection=not reload)

  if (reload):
    print("Generating new JWT")
    query = "SELECT * FROM users user WHERE user.id = ?"
    user = db.fetch_one(query, (request.user["id"],))

    print(user)

    print(bool(user))

    if (bool(user)):
      print("SET COOKIE")
      user_without_password = without_keys(user, {'password'})
      encoded_jwt = encode_jwt(user_without_password)
      response.set_cookie("jwt", encoded_jwt, path="/")
      user = user_without_password
      response.status = 200

      redirect(f'/profile/{username}')

    if (db.exception):
      response.status = 500
      return "Something went wrong"
  
  if (bool(request.user)):
    return dict(posts=posts, user=user, people=users, person=person, is_fetch=request.is_fetch, following_ids=[])
  else:
    return dict(posts=posts, person=person, people=users, is_fetch=request.is_fetch, following_ids=[])
