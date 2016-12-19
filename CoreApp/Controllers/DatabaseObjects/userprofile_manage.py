import uuid
from configparser import ConfigParser

import boto3
from boto3.dynamodb.conditions import Key
from itsdangerous import URLSafeSerializer

from CoreApp.Controllers.DatabaseObjects.table_objects import user_profile_table

config_secrets = ConfigParser()
config_secrets.read('config.ini')

dynamo_db = boto3.resource('dynamodb')


def check_if_user_exists(user_profile):
    print("Checking if user exists!")
    facebook_id = user_profile['FACEBOOK_ID']
    email_id = user_profile['EMAIL_ID']
    query_response = user_profile_table.get_item(
        Key={
            'FACEBOOK_ID': facebook_id,
            'EMAIL_ID': email_id
        }
    )

    result = {
        'status': '',
        'user_token': ''
    }
    if 'Item' not in query_response:
        print("User does not exist!")
        token = create_new_profile(user_profile)
        result['status'] = 101
        result['user_token'] = token
    else:
        print("User Exists")
        result['status'] = 102
        result['user_token'] = query_response['Item']['USER_TOKEN']

    return result


def create_new_profile(user_profile):
    token_signer = URLSafeSerializer(config_secrets["UUIDSECRET"]["secret_key"],
                                     salt=config_secrets["UUIDSECRET"]["secret_salt"])

    print("Creating a new entry for user!")

    # Generate New User ID --> Random and unique
    user_id = 'UI_' + str(uuid.uuid4())

    # Generate New User Token
    user_token = token_signer.dumps(user_id)

    # New User Record Structure
    new_user_profile = {
        'FACEBOOK_ID': user_profile['FACEBOOK_ID'],
        'USER_ID': user_id,
        'USER_NAME': user_profile['USER_NAME'],
        'EMAIL_ID': user_profile['EMAIL_ID'],
        'GENDER': user_profile['GENDER'],
        'USER_TOKEN': user_token
    }

    user_profile_table.put_item(
        Item=new_user_profile
    )

    print("New entry created!")
    return user_token


def get_user_id(user_token):
    user_id = 0
    projection_expression = "USER_ID"
    filter_expression = Key('USER_TOKEN').eq(user_token)
    response = user_profile_table.scan(
        ProjectionExpression=projection_expression,
        FilterExpression=filter_expression
    )
    for i in response['Items']:
        user_id = i["USER_ID"]
    print("The user id is ", user_id)

    return user_id


def get_user_id_given_facebook_id(facebook_id):
    print("testing the query")
    projection_expression = "USER_ID"
    filter_expression = Key('FACEBOOK_ID').eq(facebook_id)
    response = user_profile_table.scan(
        ProjectionExpression=projection_expression,
        FilterExpression=filter_expression
    )
    for i in response['Items']:
        user_id = i["USER_ID"]

    return user_id

# get_user_id("IlVJX2NhMjYzYjQyLTQ5MzctNDA1My05MTUzLTllZjY1YzE1ZDY0ZSI.urxhl2iflfL1TMTdJKhBVkX0cOQ")
# get_user_id_given_facebook_id("fb100004")
