from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewLyricForm
from .models import Lyric
import code
def index(request):
    #this will be where the discover link goes to
    return render(request, 'lyrics/index.html')

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
    form = NewLyricForm(request.POST)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = user
        instance.save()
        for item in request.POST.getlist('moods'):
            instance.moods.add(item)
        instance.save()
    return redirect('lyrics_show', instance.id)

def show(request, id):
    lyrics = Lyric.objects.get(pk=id)

    # code.interact(local=locals())
    return render(request, 'lyrics/show.html', locals())
