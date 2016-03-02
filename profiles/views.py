from django.shortcuts import render, redirect
from profiles.forms import UserSignUpForm, UserInfoEditForm, UserAboutEditForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User, About
import code


@login_required

def home(request):
     user = request.user
     if not About.objects.filter(user_id=user.pk):
        about = About.objects.create(user_id=user.pk)
     else:
        about = About.objects.get(user_id=user.pk)

     user_info_form = UserInfoEditForm(instance=user)
     user_about_form = UserAboutEditForm(instance=about)
     variable_list = {'user':user, 'about':about, 'info_form': user_info_form, 'about_form':user_about_form}
     return render(request, 'profiles/show.html', variable_list)

def cart(request):
    return None

def update_account(request):
    user = request.user
    form = UserInfoEditForm(request.POST, instance=user)
    code.interact(local=locals())
    if form.is_valid():
         instance = form.save(commit=False)
         instance.password = make_password(request.POST['password'])
         instance.save()
    return HttpResponse('')


def update_about(request):
    user = request.user
    about = About.objects.get(user_id=user.pk)
    form = UserAboutEditForm(request.POST, instance=about)
    if form.is_valid():
         instance = form.save(commit=False)
         instance.save()
        #  code.interact(local=locals())
    return HttpResponse('')



def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
         instance = form.save(commit=False)
         instance.is_active = True
         instance.save()
         return redirect('home')
    return render(request, 'profiles/signup.html', {'form': form})
