from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForms(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        fields = ['username', 'email', 'password1', 'password2']