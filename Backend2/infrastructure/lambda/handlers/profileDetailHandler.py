import boto3
import os
import json
import logging
dynamodb = boto3.resource('dynamodb')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def profileDetailHandler(body: dict):

    table = dynamodb.Table(os.environ['DYNAMODB'])

    result = table.get_item(
        Key={
            'username': body['username']
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