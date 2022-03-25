import datetime
import uuid

from bottle import post, request
from src.decorators.validate import validate
from src.globals import POSTS, USER
from src.schemas.post import PostSchema


@post("/posts")
@validate(PostSchema)
def _():
  post_id = str(uuid.uuid4())
  POSTS.insert(0 ,{ "id": post_id, "user": USER, "content": request.json.get("content"), "createdAt": datetime.datetime.now().timestamp() })
  return post_id
