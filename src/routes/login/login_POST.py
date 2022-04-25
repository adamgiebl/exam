from csv import register_dialect
from pprint import pprint

from bottle import post, redirect, request, response
from src.database.interface import DBInterface
from src.decorators.validate import validate
from src.schemas.login import LoginUserSchema
from src.utils import encode_jwt, without_keys


@post("/login")
@validate(LoginUserSchema)
def _():
  data = request.validated_data

  db = DBInterface()
  query = "SELECT * FROM users user WHERE user.email = ? AND user.password = ?"
  user = db.fetch_one(query, (data["email"], data["password"]))

  if (bool(user)):
    user_without_password = without_keys(user, {'password'})
    encoded_jwt = encode_jwt(user_without_password)
    response.set_cookie("jwt", encoded_jwt, path="/")
    response.status = 200
    return redirect('/')

      
  return redirect(f"/login?error=credentials&email={data['email']}")
