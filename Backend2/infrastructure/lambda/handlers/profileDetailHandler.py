import boto3
import os
import json
dynamodb = boto3.resource('dynamodb')


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