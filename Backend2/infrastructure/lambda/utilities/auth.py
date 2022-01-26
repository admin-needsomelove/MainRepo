import jwt
from constants import *

def verify_token_return_username(token):
    pass

def generate_token(username,password):
    token = jwt.encode({"username": username,"password": password}, SECRET_JWT_KEY, algorithm="HS256")
    #jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
    return token

