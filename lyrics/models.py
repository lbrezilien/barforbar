from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mood(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

class Genre(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

class Lyric(models.Model):
    user = models.ForeignKey(User, blank=True)
    artist = models.CharField(max_length = 300)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    moods = models.ManyToManyField(Mood, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.title




# Should I split up my models? Not sure
