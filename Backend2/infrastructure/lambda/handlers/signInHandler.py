import logging
from utilities import auth , http, ddb , exceptions
from constants import *

logger = logging.getLogger()

@exceptions.exception_handler
def signInHandler(body: dict):

    if 'password' not in body or 'username' not in body:
        raise Exception(INVALID_REQUEST_PARAMS)

    input_password = body['password']
    input_username = body['username']
    
    result = ddb.get_item({'username': input_username})
    
    logger.info("DynamoDb returned " + str(result) + "for username " + input_username)
    
    if not result or 'Item' not in result:
        raise Exception(INCORRECT_USERNAME_PASSWORD)

    if 'password' not in result['Item'] or 'username' not in result['Item']:
        logger.info("DynamoDB entry is invalid. Username or password missing in the table")
        raise Exception(CORRUPTED_DB)
    
    actual_password = result['Item']['password']
    actual_username = result['Item']['username']
    
    if input_password!=actual_password:
        logger.info("Passwords do not match")
        raise Exception(INCORRECT_USERNAME_PASSWORD)
    
    token = auth.generate_token(actual_username,actual_password)
    logger.info("Generated token : " + token)
    
    result = {
        'token': token
    }

    return http.returnHttpResponse(result)