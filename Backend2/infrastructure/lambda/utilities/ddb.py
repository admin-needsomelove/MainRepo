import boto3
import os

# get item, scan itmes, update items, put items, put items do not overwrite

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB'])

def get_item(key):
    #if item doesnt exist then return None else return item
    result = table.get_item(Key=key)

    if 'Item' not in result:
        return None
    
    return result['Item']

def put_item_do_not_overwrite(key, unique_attribute):
    result = table.put_item(
       Item=key,
       ConditionExpression='attribute_not_exists('+unique_attribute+')'
    )

    return True

