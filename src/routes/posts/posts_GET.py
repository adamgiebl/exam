from bottle import get, view
from src.globals import POSTS


@get("/posts")
@view("posts")
def _():
  return dict(posts=POSTS)
