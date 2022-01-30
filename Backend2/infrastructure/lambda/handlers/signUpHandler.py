import logging
from utilities import http , ddb , exceptions
from constants import *

logger = logging.getLogger()

@exceptions.exception_handler
def signUpHandler(body: dict):

    if 'username' not in body or 'password' not in body:
        raise Exception(INVALID_REQUEST_PARAMS)
    logger.info("Received username is " + body['username'] + " and password is " + body['password'])
    
    ddb.put_username_password({
        'username': body['username'],
        'password': body['password']
    }, 'username')

    return http.returnHttpSuccess()