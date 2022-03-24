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
  {"img": "https://pbs.twimg.com/profile_images/1414990564408262661/r6YemvF9_400x400.jpg", "title": "GitHub", "username": "github", "verified": True },
  {"img": "https://pbs.twimg.com/profile_images/1503591435324563456/foUrqiEw_400x400.jpg", "title": "Elon Musk", "username": "elonmusk", "verified": True },
  {"img": "https://pbs.twimg.com/profile_images/650743198348808192/LT6SeOJr_400x400.jpg", "title": "Cory House", "username": "housecor", "verified": False }
]

trends = [
  {"category": "Music", "title": "We Won", "tweets_count": "135K"},
  {"category": "Pop", "title": "Blue Ivy", "tweets_count": "40k"},
  {"category": "Trending in US", "title": "Denim Day", "tweets_count": "40k"},
  {"category": "Music", "title": "We Won", "tweets_count": "135K"},
  {"category": "Pop", "title": "Blue Ivy", "tweets_count": "40k"},
  {"category": "Trending in US", "title": "Denim Day", "tweets_count": "40k"},
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
@get("/app.js")
def _():
  return static_file("app.js", root=".")

##############################
@get("/images/<image_name>")
def _(image_name):
  return static_file(image_name, root="./images")

##############################
@get("/")
@view("index")
def _():
  return dict(tabs=tabs, tweets=tweets, trends=trends, people=people)



##############################
try:
  import production
  application = default_app()
except Exception as ex:
  print("Server running on development")
  run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
