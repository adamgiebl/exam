from bottle import get, request, view


@get("/login")
@view("login")
def _():
    return dict(error=request.params.get("error"), email=request.params.get("email"))
