from django.shortcuts import render
from django.http import HttpResponse

def home(request):

     return render(request, 'profiles/index.html')


def login(request):

     return HttpResponse("Hello, world. You're at the profiles index.")


def signup(request):

     return HttpResponse("Hello, world. You're at the profiles index.")


def logout(request):

     return HttpResponse("Hello, world. You're at the profiles index.")
