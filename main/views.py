from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForms

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to user profile page
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            # Process the login form
            return redirect('profile')  # Redirect to user profile page
    else:
        form = LoginForms()
    return render(request, 'main/login.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'main/home.html')
