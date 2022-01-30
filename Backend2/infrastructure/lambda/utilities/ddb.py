import boto3
import os
import botocore.exceptions
from constants import *

# get item, scan itmes, update items, put items, put items do not overwrite

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB'])

def get_item(key):
    #if item doesnt exist then return None else return item
    result = table.get_item(Key=key)

    if 'Item' not in result:
        return None
    
    return result

def put_username_password(key, unique_attribute):
    
    try:
        table.put_item(
        Item=key,
        ConditionExpression='attribute_not_exists('+unique_attribute+')'
    )
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            raise Exception(DUPLICATE_USERNAME_EXCEPTION)

def put_item(key):
    table.put_item(
       Item=key
    )

def scan_table():
    response = table.scan()
    result = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        result.extend(response['Items'])

    return result
    