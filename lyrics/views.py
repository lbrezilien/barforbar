from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewLyricForm
from .models import Lyric, Mood, Genre
import code
import json
from django.core import serializers

def index(request):

    data = serializers.serialize("json", Mood.objects.all(), fields=('title','lyric_mood'))

    # data = json.dumps(moods)
    # code.interact(local=locals())
    #this will be where the discover link goes to
    # return render(request, 'lyrics/index.html', locals())
    return HttpResponse(data, content_type='application/json')

def search(request):
    #this will be where the discover link goes to
    return render(request, 'lyrics/index.html')

@login_required
def new(request):
    form = NewLyricForm()
    return render(request, 'lyrics/new.html', locals())

@login_required
def create(request):
    user = request.user
    #add and if statement for update and create
    form = NewLyricForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = user
        instance.save()
        for mood in request.POST.getlist('moods'):
            instance.moods.add(mood)
        for genre in request.POST.getlist('genres'):
            instance.genres.add(genre)
        instance.save()
    return redirect('lyrics_show', instance.id)

def show(request, id):
    lyrics = Lyric.objects.get(pk=id)
    return render(request, 'lyrics/show.html', locals())
