import logging
import boto3
from utilities import auth , http, ddb , exceptions
from constants import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')

FAILURE_RESPONSE = {
        'authentication_success': False
}

@exceptions.exception_handler
def signInHandler(body: dict):

    if 'password' not in body or 'username' not in body:
        raise Exception(INVALID_REQUEST_PARAMS)

    input_password = body['password']
    result = ddb.get_item({'username': body['username']})
    logger.info("result from db is " + str(result))
    
    if not result or 'Item' not in result:
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