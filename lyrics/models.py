from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lyric(models.Model):
    user = models.ForeignKey(User)
    artist = models.CharField(max_length = 300)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)


# Should I split up my models? Not sure
