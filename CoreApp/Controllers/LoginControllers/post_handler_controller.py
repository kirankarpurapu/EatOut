from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
import json

def handle_post(request):
	if(request.body):
		received_json_data = json.loads(request.body.decode("utf-8"))
		app_response = {
			"marks" : received_json_data["marks"],
			"status" : "success"
		}
		print("marks from post %s" % received_json_data["marks"])
	else:
		app_response = {
			"status" : "missing post data"
		}
	return app_response	
			
	# return render(request, 'eatOutApp/index.html',context)