import jwt
from bottle import post, redirect, request, response
from src.globals import JWT_SECRET, REGEX_EMAIL, USERS


@post("/login")
def _():
    if not request.forms.get("email"):
        return redirect("/login?error=email")

    if not re.match(REGEX_EMAIL, request.forms.get("email")):
        return redirect("/login?error=email")

    password = request.forms.get("password")
    email = request.forms.get("email")

    print(password)
    
    if not password:
        return redirect(f"/login?error=user_password&email={email}")

    for user in USERS:
        if user.email == email and user.password == password:

            user_without_password = {"id": user.id, "email": user.email, "first_name": user.first_name, "last_name": user.last_name, "hex_color": user.hex_color }

            encoded_jwt = jwt.encode(user_without_password, JWT_SECRET, algorithm="HS256")
            response.set_cookie("jwt", encoded_jwt)

            print(encoded_jwt)
            
            return redirect("/")

    return redirect(f"/login?error=credentials&email={email}")
