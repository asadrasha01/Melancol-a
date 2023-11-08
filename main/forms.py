from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class LoginForms(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
