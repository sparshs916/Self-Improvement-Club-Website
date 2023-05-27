from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    #profile_image = forms.FileField() # add this field


    class Meta:
        model = User
        fields=["username","email","password1","password2"]
