import boto3
import os
import json
import logging

from utilities import http , ddb
#dynamodb = boto3.resource('dynamodb')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def profileDetailHandler(body: dict):

    #table = dynamodb.Table(os.environ['DYNAMODB'])

    """ result = table.get_item(
        Key={
            'username': body['username']
        }
    ) """
    if 'username' not in body:
        return http.returnHttpResponse({})

    result = ddb.get_item({'username': body['username']})

    return http.returnHttpResponse(result if result else {})