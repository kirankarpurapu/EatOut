from botocore.exceptions import ClientError

from CoreApp.Controllers.DatabaseObjects.userprofile_manage import get_user_id
from CoreApp.Controllers.DatabaseObjects.table_objects import restaurant_review_table as restaurant_review_table
import json
import boto3

dynamo_db = boto3.resource('dynamodb')

# sample restaurant review record
'''
{
    "RESTAURANT_ID" : "REST123",
    "ITEMS" : [{"ITEM_NAME" : "DOSA" , "ITEM_LIKE_COUNT" : 100, "ITEM_DISLIKE_COUNT" : 23},
               {"ITEM_NAME" : "IDLY" , "ITEM_LIKE_COUNT" : 200, "ITEM_DISLIKE_COUNT" : 43},
               {"ITEM_NAME" : "POORI" , "ITEM_LIKE_COUNT" : 150, "ITEM_DISLIKE_COUNT" : 04}]
}
'''


def update_restaurant_review(restaurant_id, item_name, status):
    # boolean status indicates like if it is true
    print("request for updating the reviews of ", restaurant_id, " cuisine, for the item ",
          item_name, " and the users status is ", status)
    try:
        current_review = restaurant_review_table.get_item(
            Key={
                "RESTAURANT_ID": restaurant_id
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        found_flag = False
        print("GetRestaurant review for updation succeeded:")
        print("response of get item", current_review)
        if "Item" in current_review:
            current_review = current_review["Item"]
            # work on updating the review
            items = current_review["ITEMS"]
            print("current review, ", items)
            for item in items:
                if item["ITEM_NAME"] in item_name or item_name in item["ITEM_NAME"]:
                    print("found the item")
                    if status:
                        item["ITEM_LIKE_COUNT"] += 1
                    else:
                        item["ITEM_DISLIKE_COUNT"] += 1
                    found_flag = True
                    break
            if not found_flag:
                # item not found, so should add manually
                new_item = {"ITEM_NAME": item_name}
                if status:
                    new_item["ITEM_LIKE_COUNT"] = 1
                    new_item["ITEM_DISLIKE_COUNT"] = 0
                else:
                    new_item["ITEM_LIKE_COUNT"] = 0
                    new_item["ITEM_DISLIKE_COUNT"] = 1
                items.append(new_item)

            # now update the review
            update_response = restaurant_review_table.put_item(
                Item={
                    "RESTAURANT_ID": restaurant_id,
                    "ITEMS": items,
                }
            )
            print("restaurant update response ", update_response)
        else:
            print(" this is a new restaurant")
            items = []
            single_item = {"ITEM_NAME": item_name}
            if status:
                single_item["ITEM_LIKE_COUNT"] = 1
                single_item["ITEM_DISLIKE_COUNT"] = 0
            else:
                single_item["ITEM_LIKE_COUNT"] = 0
                single_item["ITEM_DISLIKE_COUNT"] = 1
            items.append(single_item)
            update_response = restaurant_review_table.put_item(
                Item={
                    "RESTAURANT_ID": restaurant_id,
                    "ITEMS": items,
                }
            )
            print("restaurant update response ", update_response)

update_restaurant_review("REST_1236", "MASALA DOSA", False)
'''
def update_restaurant_review(request):
    # 600 series of responses
    print("updating restaurant profile")
    request_body = json.loads(request.body.decode("utf-8"))
    update_restaurant_review_response = {}
    if "USER_TOKEN" in request_body:
        user_id = get_user_id(request_body["USER_TOKEN"])
        if user_id == 0:
            print("invalid user token while updating preferences")
            update_restaurant_review_response["STATUS"] = 602
            return update_restaurant_review_response
        else:
            print("user token is correct")
            if "REVIEW" in request_body:
                review = request_body["REVIEW"]
                # work on the review

            else:
                update_restaurant_review_response["STATUS"] = 603
                return update_restaurant_review_response
    else:
        update_restaurant_review_response["STATUS"] = 602
        return update_restaurant_review_response
'''


def get_cuisines(request):
    print("request for cuisines list")
    cuisine_list_response = {}
    request_body = json.loads(request.body.decode("utf-8"))
    if "USER_TOKEN" in request_body:
        user_id = get_user_id(request_body["USER_TOKEN"])
        if user_id == 0:
            print("invalid user token while updating preferences")
            cuisine_list_response["STATUS"] = 502
            return cuisine_list_response
        else:
            cuisines = [
                {'name': 'American'},
                {'name': 'Chinese'},
                {'name': 'Italian'},
                {'name': 'Mexican'},
                {'name': 'Japanese'},
                {'name': 'Caribbean'},
                {'name': 'Spanish'},
                {'name': 'Indian'},
                {'name': 'Asian'},
                {'name': 'Jewish'},
                {'name': 'French'},
                {'name': 'Thai'},
                {'name': 'Korean'},
                {'name': 'Mediterranean'},
                {'name': 'Irish'},
                {'name': 'Seafood'},
                {'name': 'Middle Eastern'},
                {'name': 'Greek'},
                {'name': 'Vietnamese'},
                {'name': 'Russian'},
                {'name': 'Eastern European'},
                {'name': 'African'},
                {'name': 'Turkish'},
                {'name': 'Soul Food'},
                {'name': 'Continental'},
                {'name': 'Pakistani'},
                {'name': 'German'},
                {'name': 'Fillipino'},
                {'name': 'Polish'},
                {'name': 'Brazilian'},
                {'name': 'Ethiopian'},
                {'name': 'Australian'},
                {'name': 'English'},
                {'name': 'Portugese'},
                {'name': 'Egyptian'},
                {'name': 'Indonesian'},
                {'name': 'Chilean'},
                {'name': 'Hawaiian'},
            ]
            cuisine_list_response["LIST_OF_CUISINES"] = cuisines
            return cuisine_list_response

    else:
        cuisine_list_response["STATUS"] = 502
        return cuisine_list_response
