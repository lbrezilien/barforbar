
from django.contrib.auth.models import User
from .models import About
from django.forms import ModelForm


class UserSignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

class UserInfoEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']

class UserAboutEditForm(ModelForm):
    class Meta:
        model = About
        fields = ['why_quote', 'description', 'genre_interests', 'city', 'state']
