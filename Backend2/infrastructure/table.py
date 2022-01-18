from aws_cdk import (
    RemovalPolicy,
    aws_dynamodb as dynamo,
    custom_resources as cr,
    aws_logs as logs
)

def createTable(self):
    mainTable = dynamo.Table(self,"MainTable",
            partition_key=dynamo.Attribute(name="username",type= dynamo.AttributeType.STRING),
            removal_policy= RemovalPolicy.DESTROY
        )
    
    populateTableWithTestData(self,mainTable)
    
    return mainTable


def populateTableWithTestData(self,table):
    
    testData = cr.AwsCustomResource(self,'populateTestData', 
        on_create=cr.AwsSdkCall(
            service='DynamoDB',
            action='batchWriteItem',
            parameters= testDataGenerator(self,table),
            physical_resource_id=cr.PhysicalResourceId.of("dataInitializer")
        ),
        policy=cr.AwsCustomResourcePolicy.from_sdk_calls(resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE),
        log_retention=logs.RetentionDays.INFINITE

    )

def testDataGenerator(self,table):

    testData = [["insanebutsmart","zugzwang","Friendster","Soo much money","my friendster details"],
    ["joker2895","zugzwang","Customer","Soo lil money","my customer details"]
    ]

    def create_request(request_data):
        return {
                    "PutRequest": {
                        "Item": {
                            "username": {
                                "S": request_data[0]
                            },
                            "password": { 
                                "S": request_data[1]
                            },
                            "account_type": {
                                "S": request_data[2]
                            },
                            "payment_info": {
                                "S": request_data[3]
                            },
                            "details": {
                                "S": request_data[5]
                            }
                        }   
                    }
                }


    requestParams = [create_request(request_data) for request_data in testData]

    
    return {
                "RequestItems": {
                    table.table_name: requestParams
                }
            }
