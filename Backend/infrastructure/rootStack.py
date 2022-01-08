from aws_cdk import (
    # Duration,
    RemovalPolicy,
    Stack,
    aws_dynamodb as dynamo
)
from constructs import Construct
from . import lambdaFactory
from . import apiGatewayFactory

class RootStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        girls_table = dynamo.Table(self,"GirlsTable",
            partition_key=dynamo.Attribute(name="id",type= dynamo.AttributeType.STRING),
            removal_policy= RemovalPolicy.DESTROY
        )

        lambda_function = lambdaFactory.createLambda(self,girls_table)

        apiGateway = apiGatewayFactory.createApiGateway(self,lambda_function)

