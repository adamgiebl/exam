from bottle import get, view
from src.globals import POSTS, USER


@get("/")
@view("index")
def _():
  return dict(posts=POSTS, user=USER)
