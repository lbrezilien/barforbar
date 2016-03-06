
from django.contrib.auth.models import User
from .models import About
from django.forms import ModelForm, PasswordInput, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import code



class UserSignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

class UserInfoEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserInfoEditForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label
            self.fields[field].label = ""

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        widgets = {
                    'password': PasswordInput(render_value = True),
                }

class UserAboutEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserAboutEditForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label
            self.fields[field].label = ""

    class Meta:
        model = About
        fields = ['why_quote', 'description', 'genre_interests', 'city', 'state']
        widgets = {
                    'why_quote': TextInput(attrs={'Placeholder': 'Favorite Line in a song'}),
                    'description': Textarea(attrs={'Placeholder': 'A little about yourself', 'class' : 'materialize-textarea'}),
                }
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
