# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'blog/base.html') 

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    return redirect('home')

# Profile management view
@login_required
def profile(request):
    if request.method == 'POST':
        # Handle profile update logic (like email or additional fields)
        user = request.user
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')
    return render(request, 'blog/profile.html')
