from bottle import get, run


##############################
@get("/")
def _():
  return "x"

##############################



##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
