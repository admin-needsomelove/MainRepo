import logging
from utilities import auth, http , ddb

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def updateCustomerTypeHandler(body: dict):

    if 'token' not in body or 'account_type' not in body:
        logger.info("The API call was missing either token field or account_type field")
        return http.returnHttpResponse({})

    username = auth.verify_token_return_username(body['token'])

    if not username:
        logger.info("The user token was incorrect")
        return http.returnHttpResponse({})

    response = ddb.get_item({'username':username})
    item = response['Item']
    item['account_type'] = body['account_type']
    result = ddb.put_item(item)

    return http.returnHttpResponse(result)