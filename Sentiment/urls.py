from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Sentiment-home'),  # routes for /sentiment
    path('about/', views.about, name='Sentiment-about'), # routes for /sentiment/about
]