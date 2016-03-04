from django.db import models
from django.contrib.auth.models import User

class Lyric(models.Model):
    user = models.ForeignKey(User, blank=True)
    artist = models.CharField(max_length = 300)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

    def __str__(self):
            return self.title

class Mood(models.Model):
    title = models.CharField(max_length=20)
    lyrics = models.ManyToManyField(Lyric, blank=True)

    def __str__(self):
        return self.title

class Genre(models.Model):
    title = models.CharField(max_length=20)
    lyrics = models.ManyToManyField(Lyric, blank=True)

    def __str__(self):
        return self.title








# Should I split up my models? Not sure
