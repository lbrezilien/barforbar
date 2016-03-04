from django.contrib.auth.models import User
from .models import Lyric, Mood, Genre
from django import forms

class NewLyricForm(forms.ModelForm):
    moods = forms.ModelMultipleChoiceField(queryset=Mood.objects.all())
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())

    class Meta:
        model = Lyric
        widgets={
        'content': forms.Textarea(attrs={'cols': 500, 'rows': 500}),
        }
        exclude = ['user','id']
