import jwt
from constants import *

def verify_token_return_username(token):
    decoded_jwt = jwt.decode(token, SECRET_JWT_KEY, algorithms=["HS256"])
    if "username" in decoded_jwt:
        return decoded_jwt["username"]
    return None

def generate_token(username,password):
    token = jwt.encode({"username": username,"password": password}, SECRET_JWT_KEY, algorithm="HS256")
    return token

