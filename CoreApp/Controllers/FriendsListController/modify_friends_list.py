import json
from CoreApp.Controllers.DatabaseObjects.userfriends_manage import manage_friends_list
from CoreApp.Controllers.DatabaseObjects.userprofile_manage import get_user_id


def modify_friends(request):
    modify_friends_response = {}
    request_body = json.loads(request.body.decode("utf-8"))
    if 'USER_TOKEN' in request_body:
        user_id = get_user_id(request_body['USER_TOKEN'])
        if user_id == 0:
            modify_friends_response["STATUS"] = 202
            return modify_friends_response
        if 'LIST_OF_FRIENDS' in request_body:
            list_of_friends = request_body['LIST_OF_FRIENDS']
            resp = manage_friends_list(user_id, list_of_friends)
            # returning none
            if resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
                modify_friends_response["STATUS"] = 201
            else:
                modify_friends_response["STATUS"] = 202

        else:
            modify_friends_response["STATUS"] = 202
    else:
        modify_friends_response["STATUS"] = 202

    return modify_friends_response
