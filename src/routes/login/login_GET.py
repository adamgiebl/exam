from bottle import get, request, view
from src.decorators.is_fetch import is_fetch


@get("/login")
@view("login")
@is_fetch()
def _():
  error = request.params.get("error")
  email = request.params.get("email", "")
  return dict(is_fetch=request.is_fetch, error=error, email=email)
