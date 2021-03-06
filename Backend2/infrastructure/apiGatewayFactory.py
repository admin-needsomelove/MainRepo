from aws_cdk import aws_lambda, aws_apigateway

def createApiGateway(self,lambda_function: aws_lambda.Function):
    
    api = aws_apigateway.LambdaRestApi(self,"girlsApi",
    handler=lambda_function,
    proxy=False,
    default_cors_preflight_options= aws_apigateway.CorsOptions(allow_origins=aws_apigateway.Cors.ALL_ORIGINS))

    profileListResource = api.root.add_resource('profileList')
    profileListResource.add_method("POST")

    profileDetailResource = api.root.add_resource('profileDetail')
    profileDetailResource.add_method("POST")

    profileUpdateResource = api.root.add_resource('profileUpdate')
    profileUpdateResource.add_method("POST")

    signUpResource = api.root.add_resource('signUp')
    signUpResource.add_method("POST")

    signInResource = api.root.add_resource('signIn')
    signInResource.add_method("POST") 

    updateCustomerTypeResource = api.root.add_resource('updateCustomerType')
    updateCustomerTypeResource.add_method("POST")

    return api
