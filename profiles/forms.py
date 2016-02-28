
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserSignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
