from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse # import library for http response

# http request for home page
def home(request):
	return render(request, 'Sentiment/home.html', { 'title': 'Home' })

# http request for trending page
@login_required
def trending(request):
	return render(request, 'Sentiment/trending.html', { 'title': 'Trending'})

# http request for Check Random page
@login_required
def checkRandom(request):
	return render(request, 'Sentiment/checkRandom.html', { 'title': 'Check Random'})

# http request for about page
def about(request):
	return render(request, 'Sentiment/about.html', { 'title': 'About'})

# http request for contact page
def contact(request):
	return render(request, 'Sentiment/contact.html', { 'title': 'Contact'})
	
