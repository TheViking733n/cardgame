from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

@login_required
def index(request):
    return render(request, 'room/index.html')


@login_required
def create(request):
    return HttpResponse("Not yet implemented")


