from django.shortcuts import render, redirect
from profiles.forms import UserSignUpForm, UserInfoEditForm, UserAboutEditForm, myLoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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


def login(request):
    form = AuthenticationForm(request.POST or None)
    form.fields['username'].widget.attrs.update({'placeholder': 'Username:'})
    form.fields['password'].widget.attrs.update({'placeholder': 'Password:'})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('home')
            else:
                return redirect('home')


    return render(request, 'profiles/login.html', locals())


def signup(request):
    form = UserCreationForm(request.POST or None)
    form.fields['username'].widget.attrs.update({'placeholder': 'Username:'})
    form.fields['password1'].widget.attrs.update({'placeholder': 'Password:'})
    form.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password:'})

    if form.is_valid():
         instance = form.save(commit=False)
         instance.is_active = True
         instance.save()
         instance.backend = "django.contrib.auth.backends.ModelBackend"
         auth_login(request, instance)
         return redirect('home')
    return render(request, 'profiles/signup.html', {'form': form})
