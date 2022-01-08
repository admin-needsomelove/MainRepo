from aws_cdk import aws_lambda, aws_apigateway

def createApiGateway(self,lambda_function: aws_lambda.Function):
    
    api = aws_apigateway.LambdaRestApi(self,"girlsApi",
    handler=lambda_function,
    proxy=False)

    girlsResource = api.root.add_resource('girls')
    girlsResource.add_method("POST")
    return api

"""
Sample requests
{
  "artist": "yash",
  "song": "never say never",
  "id": "67738383dd",
  "priceUsdCents": "1007",
  "publisher": "yash"
  "taskType":"putGirls" 
}

{
    "taskType":"getGirls",
    "name": "yash"
}
"""
