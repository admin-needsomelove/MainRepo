import os
import logging
import jsonpickle
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from handlers import putGirls, getGirls

logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES\r' + jsonpickle.encode(dict(**os.environ)))
    logger.info('## EVENT\r' + jsonpickle.encode(event))
    logger.info('## CONTEXT\r' + jsonpickle.encode(context))
    
    options = {'getGirls' : getGirls.getGirlsHandler,
           'putGirls' : putGirls.putGirlsHandler}   

    body = jsonpickle.decode(event['body'])

    return options[body['taskType']](body)

"""
{
      "taskType":"putGirls",
      "name":"jessica",
      "age":"25",
      "color":"white"
}

{
    "taskType":"getGirls",
    "id":"7257"
}
"""