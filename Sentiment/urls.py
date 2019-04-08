from django.urls import path
from . import views
from .views import userinput

urlpatterns = [
    path('', views.home, name='Sentiment-home'),  # routes for /sentiment
    path('trending/', views.trending, name='Sentiment-trending'), # routes for /sentiment/trending
    path('search_result/', views.search_result, name='Sentiment-search_result'), # routes for /sentiment/search_result
    path('checkRandom/', views.checkRandom, name='Sentiment-checkRandom'), # routes for /sentiment/checkRandom
    path('about/', views.about, name='Sentiment-about'), # routes for /sentiment/about
    path('contact/', views.contact, name='Sentiment-contact'), # routes for /sentiment/contact
]