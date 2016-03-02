from django.shortcuts import render, redirect
from profiles.forms import UserSignUpForm, UserInfoEditForm, UserAboutEditForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .models import User


@login_required

def home(request):
     user = request.user
     about = user.about_set
     user_info_form = UserInfoEditForm(request.POST or None)
     user_about_form = UserAboutEditForm(request.POST or None)
     variable_list = {'user':user, 'about':about, 'info_form': user_info_form, 'about_form':user_about_form}

     return render(request, 'profiles/show.html', variable_list)

def cart(request):
    return #

def update_info_form(request):
    check_form_params()
    return #JSON

def update_info_form(request):
    check_form_params()
    return #JSON

def check_form_params(form):
    if form.is_valid():
         instance = form.save(commit=False)
        #  instance.is_active = True
    return instance.save()

def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
         instance = form.save(commit=False)
         instance.is_active = True
         instance.save()
         return redirect('home')
    return render(request, 'profiles/signup.html', {'form': form})
