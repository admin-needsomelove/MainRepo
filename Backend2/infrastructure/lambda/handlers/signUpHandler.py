import boto3
import os
import json
import random
import logging
dynamodb = boto3.resource('dynamodb')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def signUpHandler(body: dict):

    table = dynamodb.Table(os.environ['DYNAMODB'])

    result = table.put_item(
       Item={
            'username': body['username'],
            'password': body['password']
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