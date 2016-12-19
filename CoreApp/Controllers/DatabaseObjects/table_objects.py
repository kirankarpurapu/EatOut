import boto3

dynamo_db = boto3.resource('dynamodb')

user_profile_table = dynamo_db.Table('UserProfileTable')
user_friend_table = dynamo_db.Table('UserFriendTable')
user_preference_table = dynamo_db.Table('UserPreferenceTable')
user_review_table = dynamo_db.Table('UserReviewTable')

print("DynamoDB Connection Successful")