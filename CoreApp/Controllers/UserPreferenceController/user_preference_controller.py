from CoreApp.Controllers.DatabaseObjects.userprofile_manage import get_user_id
from CoreApp.Controllers.DatabaseObjects.table_objects import user_preference_table
import json


def update_preference(user_id, user_preferences):
    # return true if success, else return false
    # should check if the preferences are formatted correctly, user_preferences is already a JSON

    # should write an update query here

        update_response = user_preference_table.update_item(
            Key={
                'USER_ID': user_id
            },
            UpdateExpression="set PREFERENCES = :l",
            ExpressionAttributeValues={
                ':l': user_preferences
            }
        )

        print("UpdatePreference succeeded:")
        print("update preferences list response ", update_response)
        code = update_response["ResponseMetadata"]["HTTPStatusCode"]
        print("update preferenes list response ", code)
        if code == 200:
            return True
        else:
            return False


def update_user_preference(request):
    print("request for updating user preference")
    update_user_preference_response = {}
    request_body = json.loads(request.body.decode("utf-8"))
    if "USER_TOKEN" in request_body:
        user_id = get_user_id(request_body["USER_TOKEN"])
        if user_id == 0:
            print("invalid user token while updating preferences")
            update_user_preference_response["STATUS"] = 302
        else:
            if "PREFERENCES" in request_body:
                print("updating preferences of ", user_id)
                user_preferences = request_body["PREFERENCES"]
                update_status = update_preference(user_id, user_preferences)
                if update_status:
                    update_user_preference_response["STATUS"] = 301
                else:
                    update_user_preference_response["STATUS"] = 303
            else:
                update_user_preference_response["STATUS"] = 302

    else:
        update_user_preference_response["STATUS"] = 302

    return update_user_preference_response
