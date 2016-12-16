import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from CoreApp.Controllers.LoginControllers import login_controller as controller
from CoreApp.Controllers.LoginControllers import post_handler_controller as post_controller


def index(request):
    return HttpResponse("You are at index of the eatout app")


def page1(request):
    return HttpResponse("this is page 1")


def sub_page1(request):
    return HttpResponse("this is the subpage for page 1")


def details(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return controller.render_result(request, question_id)


@csrf_exempt
def handle_post(request):
    resp = post_controller.handle_post(request)
    print("views return value %s" % resp)
    return HttpResponse(json.dumps(resp), content_type = "application/json", status = 200)
