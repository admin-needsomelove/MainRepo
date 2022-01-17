from aws_cdk import (
    RemovalPolicy,
    aws_dynamodb as dynamo,
    custom_resources as cr,
    aws_logs as logs
)

def createTable(self):
    mainTable = dynamo.Table(self,"MainTable",
            partition_key=dynamo.Attribute(name="id",type= dynamo.AttributeType.STRING),
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

    testData = [["Susan","Friendster","Soo much money","insanebutsmart","zugzwang","my details"],
    ["yash","Customer","Soo little money","mememe","zugz","my customer details"]
    ]

    def create_request(request_data):
        return {
                    "PutRequest": {
                        "Item": {
                            "id": {
                                "S": request_data[0]
                            },
                            "type": { 
                                "S": request_data[1]
                            },
                            "payment_info": {
                                "S": request_data[2]
                            },
                            "username": {
                                "S": request_data[3]
                            },
                            "password": {
                                "S": request_data[4]
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
