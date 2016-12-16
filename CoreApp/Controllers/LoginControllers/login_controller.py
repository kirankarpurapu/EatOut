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
    # return 1 if no user, else return token
    return 1


def test_login(request):
    login_response = {}
    if request.body:
        print("got a new post request")
        received_json_data = json.loads(request.body.decode("utf-8"))
        print("non empty data")
        if "FACEBOOK_ID" in received_json_data:
            login_status = check_login(received_json_data["FACEBOOK_ID"])
            if login_status == 1:  # no account yet
                login_response["STATUS"] = 2
            else:  # an account exists
                login_response["STATUS"] = 1
                login_response["USER_TOKEN"] = login_status
        else:
            login_response["STATUS"] = 3

    else:
        login_response["STATUS"] = 3
    return login_response


def handle_post(request):
    return request
