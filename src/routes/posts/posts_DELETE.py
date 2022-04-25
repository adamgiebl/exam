from bottle import delete, request, response
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate


@delete("/posts/delete/<post_id>")
@authenticate()
def _(post_id):
  db = DBInterface()

  if (request.user["role"] == 'admin'):
    db.execute("DELETE FROM posts WHERE posts.id = ?", (post_id, ))
  else:
    db.execute("DELETE FROM posts WHERE posts.id = ? AND posts.user_id = ?", (post_id, request.user["id"]))
  
  
  if (not db.exception and db.cursor.rowcount > 0):
    return 'Deleted'
  else:
    response.status = 404
    return 'Not Found'
