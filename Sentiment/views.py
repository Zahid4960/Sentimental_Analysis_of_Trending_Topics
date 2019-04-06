from django.shortcuts import render

from django.http import HttpResponse # import library for http response

# http request for home page
def home(request):
	return HttpResponse('<h1> Home Page </h1>')



# http request for about page
def about(request):
	return HttpResponse('<h1> About Page </h1>')

