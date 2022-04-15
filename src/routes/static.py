from bottle import get, static_file


@get("/app.js")
def _():
  return static_file("/static/js/app.js", root=".")

@get("/spa.js")
def _():
  return static_file("/static/js/spa.js", root=".")

@get("/images/<image_name>")
def _(image_name):
  return static_file(image_name, root="./images")

@get("/tailwind.css")
def _():
    return static_file("/static/css/tailwind.css", root=".")

@get("/global.css")
def _():
    return static_file("/static/css/global.css", root=".")

@get("/index.js")
def _():
    return static_file("/static/js/index.js", root=".")

@get("/favicon.ico")
def _():
    return static_file("/static/favicon.ico", root=".")

@get("/favicon-16x16.png")
def _():
    return static_file("/static/favicon-16x16.png", root=".")

@get("/favicon-32x32.png")
def _():
    return static_file("/static/favicon-32x32.png", root=".")

@get("/global.css.map")
def _():
    return static_file("/static/css/global.css.map", root=".")

