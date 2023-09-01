from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html')
    else:
        return redirect('login')

def login(request):
    if not request.user.is_authenticated:
        return render(request, 'home/login.html')
    else:
        return redirect('index')


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)

    return redirect('index')


def newgame(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    