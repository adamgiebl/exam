from pprint import pprint

from bottle import delete, response
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate


@delete("/posts/delete/<post_id>")
@authenticate()
def _(post_id):
  db = DBInterface()
  db.execute("DELETE FROM posts WHERE posts.id = ?", (post_id,))
  
  if (not db.exception and db.cursor.rowcount > 0):
    return 'Deleted'
  else:
    response.status = 404
    return 'Not Found'
