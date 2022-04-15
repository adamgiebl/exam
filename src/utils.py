import jwt
from colorama import Fore, Style

from src.globals import JWT_SECRET


def encode_jwt(data):
  return jwt.encode(data, JWT_SECRET, algorithm="HS256")

def decode_jwt(token):
  return jwt.decode(token, JWT_SECRET, algorithms="HS256")

# from stackoverflow
def without_keys(d, keys):
  return {x: d[x] for x in d if x not in keys}

Fore

def ppprint(value, color):
  print(Style.BRIGHT)
  print(color + str(value));
  print(Style.RESET_ALL)
