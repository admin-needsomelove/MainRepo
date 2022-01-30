import botocore.exceptions
import json
import logging
from utilities import http , ddb , exceptions
from constants import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@exceptions.exception_handler
def signUpHandler(body: dict):

    if 'username' not in body or 'password' not in body:
        raise Exception(INVALID_REQUEST_PARAMS)

    try:
        ddb.put_item_do_not_overwrite({
            'username': body['username'],
            'password': body['password']
        }, 'username')
    
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            raise Exception(DUPLICATE_USERNAME_EXCEPTION)

    return http.returnHttpSuccess()