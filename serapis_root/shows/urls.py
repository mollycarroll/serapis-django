# shows/urls.py
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import views

app_name = 'shows'

urlpatterns = [
    path('', views.index, name='index'),
    path('music', views.music, name='music'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
