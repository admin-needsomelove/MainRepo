import boto3
import os
import json
import random
import logging
from utilities import auth, http
dynamodb = boto3.resource('dynamodb')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def updateCustomerTypeHandler(body: dict):

    table = dynamodb.Table(os.environ['DYNAMODB'])

    if 'token' not in body:
        return http.returnHttpResponse({})

    auth.verify_token_return_username(body['token'])

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