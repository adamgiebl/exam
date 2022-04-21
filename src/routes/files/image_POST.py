import imghdr
import os
import uuid

from bottle import post, redirect, request, response
from src.database.interface import DBInterface
from src.decorators.authenticate import authenticate


@post("/upload-image")
@authenticate()
def _():
  image = request.files.get("my_image")
  _, file_extension = os.path.splitext(image.filename)
  path = "static/images"
  
  # Validate extension
  if file_extension not in (".png", ".jpeg", ".jpg"):
    return "image not allowed"
  
  # overwrite jpg to jpeg so imghdr will pass validation
  if file_extension == ".jpg": file_extension = ".jpeg"

  image_name = request.user["username"] + file_extension

  try:
    os.remove(f"{path}/{image_name}")
  except:
    print("Couldn't remove")

  image.save(f"{path}/{image_name}")

  # Make sure that the image is actually a valid image
  # by reading its mime type
  print("imghdr.what", imghdr.what(f"{path}/{image_name}"))

  imghdr_extension = imghdr.what(f"{path}/{image_name}")
  
  if file_extension != f".{imghdr_extension}":
    print("mmm... suspicious ... it is not really an image")
    # remove the invalid image from the folder
    os.remove(f"{path}/{image_name}")
    return "mmm... got you! It was not an image"


  query_set_image = "UPDATE users SET image = ? WHERE id = ?;"

  db = DBInterface()

  print(image_name);

  db.execute(query_set_image, (image_name, request.user["id"]))

  if (db.exception):
    print(db.exception)
    response.status = 500
    return "Something went wrong"

  # SUCCESS
  return redirect(f'/profile/{request.user["username"]}')
