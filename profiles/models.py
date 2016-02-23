from django.db import models

class Contact(models.Model):
    phone =models.CharField(max_length = 13)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=13)

class About(models.Model):
    description = models.CharField(max_length = 300)
    genre_interests = models.CharField(max_length=100)
    why_quote = models.DateField()
    school= models.CharField(max_length=50)
    educational_focus = models.CharField(max_length=100)
