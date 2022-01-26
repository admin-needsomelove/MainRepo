import logging
import boto3
import os
import json
import jwt
from utilities import auth , http

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')

FAILURE_RESPONSE = {
        'authentication_success': False
}

def signInHandler(body: dict):

    table = dynamodb.Table(os.environ['DYNAMODB'])

    input_password = body['password']

    result = table.get_item(
        Key={
            'username': body['username']
        }
    )
    logger.info("result from db is " + str(result))
    if 'Item' not in result:
        return http.returnHttpResponse(FAILURE_RESPONSE)
    actual_password = result['Item']['password']
    if input_password!=actual_password:
        return http.returnHttpResponse(FAILURE_RESPONSE)
    username = result['Item']['username']
    token = auth.generate_token(username,input_password)
    
    result = {
        'authentication_success': True,
        'token': token
    }

    return http.returnHttpResponse(result)