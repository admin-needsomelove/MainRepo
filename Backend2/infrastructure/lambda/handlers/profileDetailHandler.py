import logging
from utilities import http , ddb, exceptions
from constants import *

logger = logging.getLogger()

@exceptions.exception_handler
def profileDetailHandler(body: dict):

    if 'username' not in body:
        raise Exception(INVALID_REQUEST_PARAMS)

    profile_username = body['username']

    result = ddb.get_item({'username': profile_username})

    if not result:
        logger.info('Profile not found for username ' + profile_username)
        raise Exception(NO_USER_EXIST)

    return http.returnHttpResponse(result)