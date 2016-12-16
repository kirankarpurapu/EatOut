import json


def handle_post(request):
    if request.body:
        received_json_data = json.loads(request.body.decode("utf-8"))
        app_response = {
            "marks": received_json_data["marks"],
            "status": "success"
        }
        print("marks from post %s" % received_json_data["marks"])
    else:
        app_response = {
            "status": "missing post data"
        }
    return app_response

