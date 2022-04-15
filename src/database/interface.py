import sqlite3

from bottle import response
from src.utils import Fore, ppprint


class DBInterface:
  def __init__(self):
    self.connection = sqlite3.connect("./src/database/database.sqlite")
    self.connection.row_factory = self._create_json_from_sqlite_result
    self.cursor = self.connection.cursor()
    self.exception = None
    
  def _wrap_with_try_except(self, function, close_connection):
    try:
      result = function()
      self.connection.commit()
      response.status = 200
      return result
    except Exception as ex:
      self.exception = ex
      ppprint(f"Query Error: {ex}", Fore.RED)
    finally:
      if (close_connection):
        self.connection.close()

  def execute(self, query, params=(), close_connection=True):
    def function():
      return self.cursor.execute(query, params)
    return self._wrap_with_try_except(function, close_connection)

  def fetch_one(self, query, params=(), close_connection=True):
    def function():
      return self.cursor.execute(query, params).fetchone()
    return self._wrap_with_try_except(function, close_connection)

  def fetch_all(self, query, params=(), close_connection=True):
    def function():
      return self.cursor.execute(query, params).fetchall()
    return self._wrap_with_try_except(function, close_connection)

  def _create_json_from_sqlite_result(self, cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
      d[col[0]] = row[idx]
    return d
