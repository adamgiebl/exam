from bottle import get, request, response, view, post
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate
from src.decorators.is_fetch import is_fetch


@post("/edit-post")
@authenticate()
def _():
  db = DBInterface()

  print("here")

  text = request.json.get("text")
  post_id = request.json.get("postId")

  query = """UPDATE posts SET text = ? WHERE id = ? AND user_id = ?"""

  db.execute(query, (text, post_id, request.user["id"]))

  print("here")

  if (db.exception):
    response.status = 500
    return 'Something went wrong'

  return 'ok'