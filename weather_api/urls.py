from django.urls import path
from . import views

urlpatterns = [
    path('getCurrentWeather/', views.get_current_weather, name='get_current_weather'),
]
