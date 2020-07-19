from django.contrib import admin
from .models import Show, Musician, HomePhoto, OnlineVideo, HomeText

admin.site.register(Show)
admin.site.register(HomeText)
admin.site.register(Musician)
admin.site.register(HomePhoto)
admin.site.register(OnlineVideo)
