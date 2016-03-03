from django.contrib.auth.models import User
from .models import Lyric, Mood
from django import forms

class NewLyricForm(forms.ModelForm):
    class Meta:
        model = Lyric
        moods = forms.ModelMultipleChoiceField(queryset=Mood.objects.all())
        widgets={
        'content': forms.Textarea(attrs={'cols': 500, 'rows': 500}),
        }
        exclude = ['user','id']
