import boto3

dynamo_db = boto3.resource('dynamodb')

user_profile_table = dynamo_db.Table('UserProfileTable')
user_friend_table = dynamo_db.Table('UserFriendTable')

print("DynamoDB Connection Successful")