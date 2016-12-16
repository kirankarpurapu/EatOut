import json
from django.shortcuts import render


def render_result(request, question_id):
    marks = 2 * int(question_id)
    context = {
        'marks': marks,
    }
    # raise Http404("Question does not exist")
    return render(request, 'CoreApp/index.html', context)


def check_login(facebook_id):
    # should connect to the db and return 1 if the user already exists and return 2 if it is a new user
    return 1


def get_user_token():
    return "abcdefgh"


def test_login(request):
    login_response = {}
    if request.body:
        print("got a new post request")
        received_json_data = json.loads(request.body.decode("utf-8"))
        print("non empty data")
        if "FACEBOOK_ID" in received_json_data:
            login_status = check_login(received_json_data["FACEBOOK_ID"])
            if login_status == 2:  # no account yet
                login_response["STATUS"] = 2
            elif login_status == 1:
                login_response["STATUS"] = 1
                login_response["USER_TOKEN"] = get_user_token()
        else:
            login_response["STATUS"] = 3

    else:
        login_response["STATUS"] = 3
    return login_response


def handle_post(request):
    return request
