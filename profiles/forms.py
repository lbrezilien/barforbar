
from django.contrib.auth.models import User
from .models import About
from django.forms import ModelForm, PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm




class UserSignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

class UserInfoEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        widgets = {
            'password': PasswordInput(render_value = True),
        }
class UserAboutEditForm(ModelForm):
    class Meta:
        model = About
        fields = ['why_quote', 'description', 'genre_interests', 'city', 'state']

class myLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        # widgets ={
        #     'username': TextInput(attrs={'Placeholder': 'Username'}),
        #     'password1': PasswordInput(attrs={'Placeholder': 'Password'}),
        #     'password2': PasswordInput(attrs={'Placeholder': 'Password Confirmation'}),
        #
        # }
