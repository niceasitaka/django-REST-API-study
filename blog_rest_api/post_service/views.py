from django.http.response import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render

def post_list(request):
	context = {'python_world' : 'Python'}
	return render(request, 'post_list.html', context)