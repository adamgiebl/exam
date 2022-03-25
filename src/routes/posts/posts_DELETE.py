from bottle import get, view, request, redirect, post, delete
from src.globals import POSTS
import uuid
import datetime

@delete("/posts/delete/<post_id>")
def _(post_id):
    print(post_id)
    # VALIDATE
    for index, item in enumerate(POSTS):
        if item["id"] == post_id:
            POSTS.pop(index)
            return redirect('/posts')

    print("No item found")

    # No item found
    return redirect('/posts')