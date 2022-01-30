import boto3
import logging
from utilities import http , ddb, exceptions
from constants import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@exceptions.exception_handler
def profileDetailHandler(body: dict):

    """ result = table.get_item(
        Key={
            'username': body['username']
        }
    ) """
    if 'username' not in body:
        raise Exception(INVALID_REQUEST_PARAMS)

    result = ddb.get_item({'username': body['username']})

    return http.returnHttpResponse(result if result else {})