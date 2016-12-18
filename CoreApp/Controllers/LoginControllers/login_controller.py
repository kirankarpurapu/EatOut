import json
from django.shortcuts import render
from CoreApp.Controllers.DatabaseObjects import userprofile_manage


def render_result(request, question_id):
    marks = 2 * int(question_id)
    context = {
        'marks': marks,
    }
    # raise Http404("Question does not exist")
    return render(request, 'CoreApp/index.html', context)


def test_login(request):
    login_response = {}

    if request.body:
        print("Incoming Login Request")
        user_profile = json.loads(request.body.decode("utf-8"))

        if "FACEBOOK_ID" in user_profile:
            login_response = userprofile_manage.check_if_user_exists(user_profile)
            print("Received response as ", login_response)

        else:
            login_response["STATUS"] = 103
            print("Incomplete Data in POST request")

    else:
        login_response["STATUS"] = 103
        print("Incomplete Data in POST request")

    return login_response


def handle_post(request):
    return request
