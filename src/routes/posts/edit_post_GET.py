from bottle import get, request, response, view
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate
from src.decorators.is_fetch import is_fetch


@get("/edit-post/<post_id>")
@view("edit-post")
@authenticate()
@is_fetch()
def _(post_id):
  db = DBInterface()

  query = """SELECT * FROM posts WHERE id = ? AND user_id = ?"""

  post = db.fetch_one(query, (post_id ,request.user["id"]))
  print(post)
  if (db.exception):
    response.status = 500
    return 'Something went wrong'

  return dict(post=post, user=request.user, is_fetch=request.is_fetch)