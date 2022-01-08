from aws_cdk import Duration, aws_dynamodb, aws_iam as iam, aws_lambda
from aws_cdk.aws_apigateway import ApiDefinition 

def createLambda(self,table: aws_dynamodb.Table):

    lambdaRole = iam.Role(self,'lambaExecutionRole',
    assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
    managed_policies=[iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")]
    )

    lambdaRole.add_to_policy(
        iam.PolicyStatement(
        resources= [table.table_arn],
        actions= ['dynamoDB:*'],
        effect= iam.Effect.ALLOW
        )
    )

    lambdaLayer = aws_lambda.LayerVersion(self, 'lambda-layer',
    code = aws_lambda.AssetCode.from_asset('./infrastructure/lambda/layer/python.zip'),
    compatible_runtimes=[aws_lambda.Runtime.PYTHON_3_9]
    )


    apiFunction = aws_lambda.Function(
        self, 'girlsLambdaFunction',
        runtime= aws_lambda.Runtime.PYTHON_3_9,
        handler= "main.lambda_handler",
        code= aws_lambda.Code.from_asset('./infrastructure/lambda'),
        role= lambdaRole,
        layers=[lambdaLayer],
        timeout= Duration.seconds(20)
    )

    apiFunction.add_environment("DYNAMODB", table.table_name)

    return apiFunction
