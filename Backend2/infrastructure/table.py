from aws_cdk import (
    RemovalPolicy,
    aws_dynamodb as dynamo,
    custom_resources as cr
)

def createTable(self):
    mainTable = dynamo.Table(self,"MainTable",
            partition_key=dynamo.Attribute(name="id",type= dynamo.AttributeType.STRING),
            removal_policy= RemovalPolicy.RETAIN
        )
    
    populateTableWithTestData(self,mainTable)
    
    return mainTable


def populateTableWithTestData(self,table):
    
    testData = cr.AwsCustomResource(self,'populateTestData', 
        on_create=cr.AwsSdkCall(
            service='DynamoDB',
            action='putItem',
            parameters= {
                'TableName': table.table_name,
                'Item': { 'id': {'S': 'Custom resources work!'}}
            },
            physical_resource_id=cr.PhysicalResourceId.of("dataInitializer")
        ),
        policy=cr.AwsCustomResourcePolicy.from_sdk_calls(
        resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE
    )
    )

