from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')


def room(request):
    username = request.GET.get('username')
    room_name = request.GET.get('room_name')
    return render(request, 'chat/messages.html', {
        'room_name': room_name,
        'username': username,
    })
