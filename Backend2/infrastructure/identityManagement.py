""" from aws_cdk import (
    RemovalPolicy,
    aws_cognito as cognito
)

def setupUsers(self):
    
    #User Pool
    userPool = cognito.UserPool(self, 'userpool',
    user_pool_name='my_user_pool',
    self_sign_up_enabled= True,
    sign_in_aliases=cognito.SignInAliases(email=True),
    auto_verify=cognito.AutoVerifiedAttrs(email=True),
    standard_attributes=cognito.StandardAttributes(
        email=cognito.StandardAttribute(
            required=True,
            mutable=True
        )),
    password_policy=cognito.PasswordPolicy(min_length=6,require_lowercase=True,require_digits=True,require_symbols=False,require_uppercase=False),
    removal_policy=RemovalPolicy.RETAIN,
    account_recovery=cognito.AccountRecovery.EMAIL_ONLY
    )
    
    clientReadAttribs = (cognito.ClientAttributes()).with_standard_attributes(given_name=True,family_name=True,email=True,address=True,
    birthdate=True, gender=True, locale=True, middle_name=True, fullname=True,
    nickname=True,phone_number=True, profile_page=True,profile_picture=True, preferred_username=True,
    timezone=True, last_update_time=True, website=True, phone_number_verified=True,email_verified=True)
    
    clientWriteAttribs = (cognito.ClientAttributes()).with_standard_attributes(given_name=True,family_name=True,email=True,address=True,
    birthdate=True, gender=True, locale=True, middle_name=True, fullname=True,
    nickname=True,phone_number=True, profile_page=True,profile_picture=True, preferred_username=True,
    timezone=True, last_update_time=True, website=True, phone_number_verified=False,email_verified=False)

    userPoolClient = cognito.UserPoolClient(self, "userPoolClient",
    user_pool=userPool,
    auth_flows=cognito.AuthFlow(admin_user_password=True, user_srp=True, custom=True),
    supported_identity_providers=[cognito.UserPoolClientIdentityProvider.COGNITO],
    read_attributes=clientReadAttribs,
    write_attributes=clientWriteAttribs)

    userPool.add_client(userPoolClient.user_pool_client_id, o_auth=cognito.OAuthSettings(flows=cognito.OAuthFlows(authorization_code_grant=True),scopes= [cognito.OAuthScope(cognito.OAuthScope.OPENID)],callback_urls=)) """