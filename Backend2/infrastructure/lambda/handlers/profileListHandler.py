import json
import logging
from utilities import exceptions , ddb

logger = logging.getLogger()

@exceptions.exception_handler
def profileListHandler(body: dict):

    result = ddb.scan_table()

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

