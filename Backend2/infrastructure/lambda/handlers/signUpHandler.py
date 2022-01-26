import botocore.exceptions
import json
import logging
from utilities import http , ddb

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def signUpHandler(body: dict):

    if 'username' not in body or 'password' not in body:
        return http.returnHttpResponse({})

    try:
        result = ddb.put_item_do_not_overwrite({
            'username': body['username'],
            'password': body['password']
        }, 'username')
    
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return http.returnHttpResponse({"Error":"Duplicate Username"})

    return http.returnHttpResponse(result)