from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Show, Musician, HomePhoto, OnlineVideo


def index(request):
    show_list = Show.objects.order_by('show_date')
    members = Musician.objects.order_by('name')
    banner = HomePhoto.objects.all
    context = {
        'show_list': show_list,
        'members': members,
        'banner': banner,
    }
    return render(request, 'shows/index.html', context)


def music(request):
    video_list = OnlineVideo.objects.order_by('date')

    context = {
        'video_list': video_list,
    }

    return render(request, 'shows/music.html', context)
