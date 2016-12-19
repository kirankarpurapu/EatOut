import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from CoreApp.Controllers.LoginControllers import login_controller as login_controller
from CoreApp.Controllers.FriendsListController import modify_friends_list as modify_friends_list_controller
from CoreApp.Controllers.UserPreferenceController import user_preference_controller as user_preference_controller


@csrf_exempt
def handle_post(request):
    resp = login_controller.handle_post(request)
    print("views return value %s" % resp)
    return HttpResponse(json.dumps(resp), content_type="application/json", status=200)


@csrf_exempt
def test_login_user(request):
    resp = login_controller.test_login(request)
    return HttpResponse(json.dumps(resp), content_type="application/json", status=200)


@csrf_exempt
def update_friends(request):
    resp = modify_friends_list_controller.modify_friends(request)
    return HttpResponse(json.dumps(resp), content_type="application/json", status=200)

@csrf_exempt
def update_preference(request):
    resp = user_preference_controller.update_user_preference(request)
    return HttpResponse(json.dumps(resp), content_type="application/json", status=200)
