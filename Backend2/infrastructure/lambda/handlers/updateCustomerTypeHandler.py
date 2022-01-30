import logging
from utilities import auth, http , ddb, exceptions
from constants import *

logger = logging.getLogger()

@exceptions.exception_handler
def updateCustomerTypeHandler(body: dict):

    if 'token' not in body or 'account_type' not in body:
        logger.info("The API call was missing either token field or account_type field")
        raise Exception(INVALID_REQUEST_PARAMS)

    username = auth.verify_token_return_username(body['token'])

    if not username:
        logger.info("The user token was wrong or corrupted")
        raise Exception(CORRUPTED_BAD_TOKEN)

    response = ddb.get_item({'username':username})

    if not response:
        logger.info("User not found in the DDB for username " + username)
        raise Exception(NO_USER_EXIST)

    item = response['Item']
    item['account_type'] = body['account_type']
    result = ddb.put_item(item)

    return http.returnHttpResponse(result)