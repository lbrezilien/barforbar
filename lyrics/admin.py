from django.contrib import admin
from .models import Mood, Lyric, Genre
# Register your models here.
admin.site.register(Mood)
admin.site.register(Lyric)
admin.site.register(Genre)
