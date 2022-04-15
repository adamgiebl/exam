from bottle import get, request, view
from src.decorators.is_fetch import is_fetch


@get("/login")
@view("login")
@is_fetch()
def _():
    return dict(is_fetch=request.is_fetch)
