# shows/urls.py

from django.urls import path

from . import views

app_name = 'shows'

urlpatterns = [
    path('', views.index, name='index'),
    path('music', views.music, name='music'),
]
