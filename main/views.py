from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegisterForm, LoginForms
from .models import *

def home(request):
    return render(request, 'main/home.html')

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

def search_results(request):
    return render(request, 'main/search_results.html')

def user_profile(request):
    return render(request, 'main/user_profile.html')

def follow_user(request, user_id):
    user_to_follow = CustomUser.objects.get(id=user_id)
    request.user.following.add(user_to_follow)
    return redirect('profile', user_id=user_id)

def unfollow_user(request, user_id):
    user_to_unfollow = CustomUser.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return redirect('profile', user_id=user_id)

def like_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    request.user.liked_trips.add(trip)
    return redirect('trip_detail', trip_id=trip_id)

def unlike_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    request.user.liked_trips.remove(trip)
    return redirect('trip_detail', trip_id=trip_id)

def trip_detail_view(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'trip.html', {'trip': trip})