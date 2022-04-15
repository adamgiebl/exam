import datetime
import uuid

from bottle import post, request
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate
from src.decorators.validate import validate
from src.schemas.post import PostSchema


@post("/posts")
@authenticate()
@validate(PostSchema)
def _():
  post_id = str(uuid.uuid4())
  post_text = request.validated_data.get("text")
  post_created_at = int(datetime.datetime.now().timestamp())
  user_id = request.user['id']


  db = DBInterface()
  db.execute("INSERT INTO posts VALUES (?, ?, ?, ?)", (post_id, post_text, user_id, post_created_at))


  return post_id
