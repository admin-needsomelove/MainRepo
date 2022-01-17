from aws_cdk import (
    # Duration,
    RemovalPolicy,
    Stack,
    aws_dynamodb as dynamo
)
from constructs import Construct

from . import identityManagement
from . import table
from . import lambdaFactory
from . import apiGatewayFactory

class RootStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        mainTable = table.createTable(self)

        lambdaFunction = lambdaFactory.createLambda(self,mainTable)

        apiGateway = apiGatewayFactory.createApiGateway(self,lambdaFunction)

        ##userManager = identityManagement.setupUsers(self)
    
    

