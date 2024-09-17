from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles
from datadog_api_client.v2.model.roles_type import RolesType
from datadog_api_client.v2.model.service_account_create_attributes import (
ServiceAccountCreateAttributes,
)
from datadog_api_client.v2.model.service_account_create_data import (
ServiceAccountCreateData,
)
from datadog_api_client.v2.model.service_account_create_request import (
ServiceAccountCreateRequest,
)
from datadog_api_client.v2.model.user_relationships import UserRelationships
from datadog_api_client.v2.model.users_type import UsersType
from datadog_api_client.v2.api.roles_api import RolesApi
import logging
import boto3
import os

# logging.basicConfig(
#       level=logging.DEBUG,
#       format='%{asctime}s - %{levelname}s - %{message}s',
#       style='{'
# )

# Set the environment variables paths for api and app keys
os.environ['API_KEY'] = '/datadog/dpe-cd/api_key'
os.environ['APP_KEY'] = '/datadog/dpe-cd/app_key'

# Set up the AWS SSM client
ssm = boto3.client('ssm')

# Get the values of the SSM parameters
api_key = ssm.get_parameter(Name=os.environ['API_KEY'], WithDecryption=True)['Parameter']['Value']
app_key = ssm.get_parameter(Name=os.environ['APP_KEY'], WithDecryption=True)['Parameter']['Value']

ROLE_DATA_ATTRIBUTES_NAME = "Datadog Standard"

configuration = Configuration()
configuration.api_key["apiKeyAuth"] = api_key
configuration.api_key["appKeyAuth"] = app_key
with ApiClient(configuration) as api_client:
       api_instance = RolesApi(api_client)
       response = api_instance.list_roles(
           filter= ROLE_DATA_ATTRIBUTES_NAME,
       )

role_id = response['data'][0]['id']

# there is a valid "role" in the system
ROLE_DATA_ID = role_id

body = ServiceAccountCreateRequest(
    data=ServiceAccountCreateData(
        type=UsersType.USERS,
        attributes=ServiceAccountCreateAttributes(
            name="ddserviceaccount",
            email="ddserviceaccount@toyota.com",
            service_account=True,
        ),
        relationships=UserRelationships(
            roles=RelationshipToRoles(
                data=[
                    RelationshipToRoleData(
                        id=ROLE_DATA_ID,
                        type=RolesType.ROLES,
                    ),
                ],
            ),
        ),
    ),
)

configuration = Configuration()
configuration.api_key["apiKeyAuth"] = api_key
configuration.api_key["appKeyAuth"] = app_key
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.create_service_account(body=body)

print(response)       
