from django.shortcuts import render, redirect
from profiles.forms import UserSignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from .models import User

@login_required
def home(request):
     item = User._meta.get_fields()
     users = User.objects.all()
     return render(request, 'profiles/index.html', {'users':users, 'item':item})


def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
         instance = form.save(commit=False)
         instance.is_active = True
         instance.save()
         return redirect('home')
        # email = request.POST['email']
        # username = request.POST['username']
        # password = request.POST['password']
        # user = User.objects.create_user(email=email, username=username, password=password)
        # login(request, f)

    return render(request, 'profiles/signup.html', {'form': form})
