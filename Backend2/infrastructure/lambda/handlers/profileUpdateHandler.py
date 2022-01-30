import boto3
import os
import json
import random
import logging
from utilities import exceptions

dynamodb = boto3.resource('dynamodb')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

@exceptions.exception_handler
def profileUpdateHandler(body: dict):

    table = dynamodb.Table(os.environ['DYNAMODB'])

    result = table.update_item(
        Key={'username':body['username']},
        AttributeUpdates={
            'details':{
                'name': body['name'],
                'age': body['age'],
                'summary': body['summary'],
                'email': body['email'],
                'video_link': body['video_link'],
                'photo_links': body['photo_links']
            }
        }
    )

    response = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(result)
    }

    return response