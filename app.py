from bottle import default_app, get, run, static_file, view

##############################
tabs = [
  {"icon": "fas fa-home fa-fw", "title": "Home", "id":"home"},
  {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore"},
  {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications"},
  {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages"},
  {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks"},
  {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists"},
  {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile"},
  {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more"}
]

people = [
  {"src": "stephie.png", "name": "Stephie Jensen", "handle": "@sjensen"},
  {"src": "monk.jpg", "name": "Adrian Monk", "handle": "@detective :)"},
  {"src": "kevin.jpg", "name": "Kevin Hart", "handle": "@miniRock"}
]

trends = [
  {"top": "Music", "title": "We Won", "bottom": "135K Tweets"},
  {"top": "Pop", "title": "Blue Ivy", "bottom": "40k tweets"},
  {"top": "Trending in US", "title": "Denim Day", "bottom": "40k tweets"},
]

tweets = [
  {"src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
  {"src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
  {"src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
  {"src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
  {"src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
  {"src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
  {"src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
  {"src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
  {"src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
  {"src":"6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"barackobama", "date":"Feb 20", "text":"The Ukrainian people need our help. If you’re looking for a way to make a difference, here are some organizations doing important work.", "image":"1.jpg"},
  {"src":"2.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"joebiden", "date":"Mar 3", "text":"Richard Hunt is one of the greatest artists Chicago has ever produced, and I couldn’t be prouder that his “Book Bird” sculpture will live outside of the newest @ChiPubLibbranch at the Obama Presidential Center. I hope it inspires visitors for years to come."},
  {"src":"3.jpg", "user_first_name":"Joe Biden", "user_last_name":"Biden", "user_name":"elonmusk", "date":"Mar 7", "text":"Last year has been the best year for manufacturing jobs and trucking jobs since 1994."},
]

##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")

##############################
@get("/images/<image_name>")
def _(image_name):
  return static_file(image_name, root="./images")

##############################
@get("/")
@view("index")
def _():
  return dict(tabs=tabs, tweets=tweets)



##############################
try:
  import production
  application = default_app()
except Exception as ex:
  print("Server running on development")
  run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
