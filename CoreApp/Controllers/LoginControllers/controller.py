from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

def render_result(request, question_id):
	marks = 2 * int(question_id)
	# template = loader.get_template('eatOutApp/index.html')
	context = {
		'marks' : marks,
	}
	# raise Http404("Question does not exist")
	return render(request, 'eatOutApp/index.html', context)

