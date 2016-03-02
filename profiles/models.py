from django.db import models
from django.contrib.auth.models import User


class About(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length = 300, blank=True)
    genre_interests = models.CharField(max_length=100, blank=True)
    why_quote = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
