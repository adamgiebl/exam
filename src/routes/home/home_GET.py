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

  query_posts_users = """SELECT post.id, post.text, post.created_at, user.last_name ,user.first_name, user.image, user.hex_color, user.username
  FROM posts post
  JOIN users user WHERE user.id = post.user_id
  ORDER BY post.created_at DESC"""

  posts = db.fetch_all(query_posts_users, close_connection=False)

  query_people = "SELECT users.first_name, users.last_name, users.username, users.id, users.image, users.hex_color FROM users"

  query_people_authenticated = """
    SELECT users.first_name, users.last_name, users.username, users.id, users.image, users.hex_color 
    FROM users
    LEFT JOIN followers ON followers.followee_id = users.id
    WHERE users.id != ?
    GROUP BY users.id
    LIMIT 10
  """

  query_people_following = """
    SELECT users.first_name, users.last_name, users.username, users.id, users.image, users.hex_color 
    FROM users
    LEFT JOIN followers ON followers.followee_id = users.id
    WHERE users.id != ? AND followers.follower_id = ?
    GROUP BY users.id
  """

  people = []
  following = []

  if (request.user):
    people = db.fetch_all(query_people_authenticated, (request.user['id'], ), close_connection=False)
    following = db.fetch_all(query_people_following, (request.user['id'], request.user['id']))
  else:
    people = db.fetch_all(query_people)


  following_ids = [d['id'] for d in following]

  if (db.exception):
    response.status = 500
    return "Something went wrong"
  
  if (bool(request.user)):
    return dict(posts=posts, user=request.user, people=people, following=following, is_fetch=request.is_fetch, following_ids=following_ids)
  else:
    return dict(posts=posts, people=people, is_fetch=request.is_fetch, following_ids=[])
 
