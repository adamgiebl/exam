from bottle import get, request, view
from src.decorators.is_fetch import is_fetch


@get("/signup")
@view("signup")
@is_fetch()
def _():
    error = request.params.get("error")
    return dict(error=error, is_fetch=request.is_fetch)
