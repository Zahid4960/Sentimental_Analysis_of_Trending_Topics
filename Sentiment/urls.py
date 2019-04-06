from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Sentiment-home'),  # routes for /sentiment
    path('trending/', views.trending, name='Sentiment-trending'), # routes for /sentiment/trending
    path('checkRandom/', views.checkRandom, name='Sentiment-checkRandom'), # routes for /sentiment/checkRandom
    path('about/', views.about, name='Sentiment-about'), # routes for /sentiment/about
    path('contact/', views.contact, name='Sentiment-contact'), # routes for /sentiment/contact
]