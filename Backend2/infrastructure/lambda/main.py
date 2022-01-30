import os
import logging
import jsonpickle
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from handlers.profileDetailHandler import profileDetailHandler
from handlers.profileListHandler import profileListHandler
from handlers.profileUpdateHandler import profileUpdateHandler
from handlers.signUpHandler import signUpHandler
from handlers.signInHandler import signInHandler
from handlers.updateCustomerTypeHandler import updateCustomerTypeHandler
from constants import *
from utilities import exceptions

logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES\r' + jsonpickle.encode(dict(**os.environ)))
    logger.info('## EVENT\r' + jsonpickle.encode(event))
    logger.info('## CONTEXT\r' + jsonpickle.encode(context))

    path = event['path'] #should be something like profileList
    
    options = {
           PROFILE_LIST_PATH : profileListHandler,
           PROFILE_DETAIL_PATH : profileDetailHandler,
           PROFILE_UPDATE_PATH : profileUpdateHandler,
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

"""
/profileList
empty body

/profileUpdate
{
    "username":"friendster_username",
    "name":"yash",
    "age":"25",
    "email":"yash@blah.com",
    "summary":"blah blah blah",
    "video_link":"url video",
    "photo_links":"photo links"
}

/profileDetail
{
    "username":"friendster_username"
}


"""