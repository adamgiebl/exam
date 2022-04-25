import datetime
import random
import uuid

from bottle import post, redirect, request
from src.database.interface import DBInterface
from src.decorators.validate import validate
from src.schemas.signup import SignupUserSchema


@post("/signup")
@validate(SignupUserSchema)
def _():
  user = request.validated_data

  user_id = str(uuid.uuid4())

  created_at = int(datetime.datetime.now().timestamp())

  hex_color = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])

  db = DBInterface()

  query = "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
  db.execute(query, (user_id, user["username"], user["first_name"], user["email"], user["last_name"], user["password"], hex_color, created_at, None, "user", user["bio"]))


  if (db.exception):
    return redirect(f"/signup?error=already_exists")

  return redirect('/')
