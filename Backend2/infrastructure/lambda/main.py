import os
import logging
import jsonpickle
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from handlers import profileListHandler , profileDetailHandler, profileUpdateHandler
from constants import PROFILE_LIST_PATH , PROFILE_DETAIL_PATH, PROFILE_UPDATE_PATH

logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES\r' + jsonpickle.encode(dict(**os.environ)))
    logger.info('## EVENT\r' + jsonpickle.encode(event))
    logger.info('## CONTEXT\r' + jsonpickle.encode(context))

    path = event['path'] #should be profileList, profileDetail, profileUpdate
    
    options = {PROFILE_LIST_PATH : profileListHandler.profileListHandler,
           PROFILE_DETAIL_PATH : profileDetailHandler.profileDetailHandler,
           PROFILE_UPDATE_PATH : profileUpdateHandler.profileUpdateHandler}   

    #because profileList has no body
    logger.info("The path is " + path)
    if path != PROFILE_LIST_PATH:
        body = jsonpickle.decode(event['body'])
    else:
        body = None

    return options[path](body)

"""
{
      "taskType":"putGirls",
      "name":"jessica",
      "age":"25",
      "color":"white"
}


"""

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