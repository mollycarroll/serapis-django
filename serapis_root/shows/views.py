from django.shortcuts import render
from django.http import HttpResponse
from .models import Show


def index(request):
    show_list = Show.objects.order_by('show_date')
    context = {'show_list': show_list}
    return render(request, 'shows/index.html', context)


def music(request):
    return render(request, 'shows/music.html')
