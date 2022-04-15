from bottle import post, request, response, view
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate
from src.decorators.is_fetch import is_fetch


@post("/follow/<username>")
@authenticate()
def _(username):
  db = DBInterface()

  query_user_by_username = "SELECT user.id FROM users user WHERE user.username = ?"

  followee = db.fetch_one(query_user_by_username, (username,), close_connection=False)

  print(followee);
  print(request.user)

  db.execute("INSERT INTO followers VALUES (null, ?, ?)", (request.user['id'], followee['id']))

  if (db.exception):
    response.status = 500
    return 'Something went wrong'

  return 'ok'
