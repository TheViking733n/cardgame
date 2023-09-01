from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from .models import Room
from random import randint
from datetime import datetime, timedelta, timezone

def getRandomRoomId():
    return randint(1000, 9999)

def getUtcTimestamp():
    '''Returns the current UTC timestamp in seconds'''
    return int(datetime.now(timezone.utc).timestamp())

# Create your views here.

@login_required
def index(request):
    return render(request, 'room/index.html')


@login_required
def create(request):
    if request.method == 'POST':
        room = Room()
        room.id = getRandomRoomId()
        room.creator = request.user.email
        room.players = {
            request.user.email: {
                'fname': request.user.first_name,
                'lname': request.user.last_name,
                'profile_url': request.user.socialaccount_set.all()[0].get_avatar_url()
            }
        }
        room.lastSeen = {
            request.user.email: str(getUtcTimestamp())
        }
        room.config = {
            'max_show_value': 5,
        }
        room.save()
        return redirect('waitingRoom', room.id)
    else:
        return redirect('roomIndex')
    

@login_required
def waitingRoom(request, room_id):
    try:
        room = Room.objects.get(id=room_id)
        room.lastSeen[request.user.email] = str(getUtcTimestamp())
        if request.user.email not in room.players:
            room.players[request.user.email] = {
                'fname': request.user.first_name,
                'lname': request.user.last_name,
                'profile_url': request.user.socialaccount_set.all()[0].get_avatar_url()
            }
        room.save()
        return render(request, 'room/waiting_room.html', {
            'room': room,
        })
    except Room.DoesNotExist:
        return HttpResponse('Room does not exist')


@login_required
def status(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    
    try:
        room_id = request.GET.get('room_id')
        room = Room.objects.get(id=room_id)
        room.lastSeen[request.user.email] = str(getUtcTimestamp())
        room.save()
        return JsonResponse(room.players)
    
    except Room.DoesNotExist:
        return HttpResponse('Room does not exist')


@login_required
def update(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    room_id = request.POST.get('room_id')


