import json

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.safestring import mark_safe
User = get_user_model()

def index(request):
    return render(request, 'chat/index.html', {})

@login_required
def room(request, room_name):
    if room_name == 'home':
        all_users = User.objects.exclude(username=request.user.username)
        return render(request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name)),
            'username': mark_safe(json.dumps(request.user.username)),
            'all_users':all_users,
        })
    else:
        return redirect('/')