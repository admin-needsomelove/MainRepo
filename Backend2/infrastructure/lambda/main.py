import os
import logging
import jsonpickle
from handlers.profileDetailHandler import profileDetailHandler
from handlers.profileListHandler import profileListHandler
from handlers.signUpHandler import signUpHandler
from handlers.signInHandler import signInHandler
from handlers.updateCustomerTypeHandler import updateCustomerTypeHandler
from constants import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES\r' + jsonpickle.encode(dict(**os.environ)))
    logger.info('## EVENT\r' + jsonpickle.encode(event))
    logger.info('## CONTEXT\r' + jsonpickle.encode(context))

    path = event['path'] #should be something like profileList
    
    options = {
           PROFILE_LIST_PATH : profileListHandler,
           PROFILE_DETAIL_PATH : profileDetailHandler,
           SIGNUP_PATH: signUpHandler,
           SIGNIN_PATH: signInHandler,
           UPDATE_CUSTOMER_TYPE_PATH: updateCustomerTypeHandler
           }   

    #because profileList has no body
    PATHS_WITH_NO_EXPECTED_BODY = set([PROFILE_LIST_PATH])
    if path not in PATHS_WITH_NO_EXPECTED_BODY:
        body = jsonpickle.decode(event['body'])
    else:
        body = None

    return options[path](body)

