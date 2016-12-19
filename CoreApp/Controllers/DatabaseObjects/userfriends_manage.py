from CoreApp.Controllers.DatabaseObjects.table_objects import user_friend_table as friend_table
from CoreApp.Controllers.DatabaseObjects.userprofile_manage import get_user_id_given_facebook_id


def manage_friends_list(user_id, list_of_friends):
    # list is a list of facebook ids, should map them to app_ids and store them in the database
    list_of_friends_user_ids = []
    update_response = {}
    for facebook_id in list_of_friends:
        user_id_of_friend = get_user_id_given_facebook_id(facebook_id)
        list_of_friends_user_ids.append(user_id_of_friend)

        update_response = friend_table.update_item(
            Key={
                'USER_ID': user_id
            },
            UpdateExpression="set FRIENDS_LIST = :l",
            ExpressionAttributeValues={
                ':l': list_of_friends_user_ids
            }
        )

        print("UpdateItem succeeded:")
        print("update friends list response ", update_response)

    return update_response

# newlist = ["fb100004", "fb100001", "fb100003"]
# manage_friends_list("fb100002", newlist)
