import json
import re

import jwt
from bottle import (error, get, post, redirect, request, response, run,
                    static_file, view)

from .globals import JWT_SECRET, REGEX_EMAIL, USERS
from .models import User


@get("/signup")
@view("signup")
def _():
    return

@post("/signup")
def _():
    if not re.match(REGEX_EMAIL, request.forms.get("email")):
        return "not valid"

    user_email = request.forms.get("email")
    first_name = request.forms.get("first_name")
    last_name = request.forms.get("last_name")
    password = request.forms.get("password")

    if not first_name or not last_name or not password:
        return "Invalid"

    user = User(user_email, first_name, last_name, password);
    
    USERS.append(user)

    user_without_password = {"id": user.id, "email": user.email, "first_name": user.first_name, "last_name": user.last_name, "hex_color": user.hex_color }

    encoded_jwt = jwt.encode(user_without_password, JWT_SECRET, algorithm="HS256")
    response.set_cookie("jwt", encoded_jwt)

    return redirect('/')
