
from bottle import get, request, view
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate
from src.decorators.is_fetch import is_fetch


@get("/users")
@view("users")
@authenticate()
@is_fetch()
def _():

  db = DBInterface()

  query = "SELECT * FROM users"

  users = db.fetch_all(query)

  if (db.exception):
    print(db.exception)

  return dict(users=users, user=request.user, is_fetch=request.is_fetch)
