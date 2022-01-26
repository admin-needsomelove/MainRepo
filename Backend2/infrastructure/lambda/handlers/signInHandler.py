import logging
import boto3
import os
import json
import jwt
from constants import SECRET_JWT_KEY

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')

authentication_success = False
token = "bullshit"

def generate_token(username,password):
    token = jwt.encode({"username": username,"password": password}, SECRET_JWT_KEY, algorithm="HS256")
    #jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
    return token

def signInHandler(body: dict):

    table = dynamodb.Table(os.environ['DYNAMODB'])

    input_password = body['password']

    result = table.get_item(
        Key={
            'username': body['username']
        }
    )
    logger.info("result from db is " + str(result))
    if 'Item' in result:
        username = result['Item']['username']
        actual_password = result['Item']['password']
        global token
        token = generate_token(username,input_password)
        if input_password==actual_password:
            global authentication_success
            authentication_success = True

    result = {
        'authentication_success': authentication_success,
        'token':token
    }

    response = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(result)
    }

    return response