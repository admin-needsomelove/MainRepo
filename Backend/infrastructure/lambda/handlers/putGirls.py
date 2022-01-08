import boto3
import os
import json
import random
dynamodb = boto3.resource('dynamodb')

def putGirlsHandler(body: dict):

    table = dynamodb.Table(os.environ['DYNAMODB'])

    result = table.put_item(
       Item={
            'id': str(random.randint(1,100000)),
            'name': body['name'],
            'details': {
                'age': body['age'],
                'color': body['color']
            }
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