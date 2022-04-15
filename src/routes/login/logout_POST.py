from bottle import post, redirect, response


@post("/logout")
def _():
    response.delete_cookie("jwt")
    return redirect('/')
