import json

def returnHttpResponse(body):
    return {
        'isBase64Encoded': False,
        'statusCode': 201,
        'headers': {
            'Content-Type': 'text/plain',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body)
    }