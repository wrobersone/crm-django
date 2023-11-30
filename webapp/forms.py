from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# Register a User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Login a User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# Create A Record
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'country']

# Update A Record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'country']