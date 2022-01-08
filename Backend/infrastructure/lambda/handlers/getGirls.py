import boto3
import os
import json
dynamodb = boto3.resource('dynamodb')


def getGirlsHandler(body: dict):

    table = dynamodb.Table(os.environ['DYNAMODB'])

    result = table.get_item(
        Key={
            'id': body['id']
        }
    )

    response = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': json.dumps(result)
    }

    return response