from rooms.models import Room
from django.http import Http404
from django.shortcuts import render

def home(request):
    rooms= Room.objects.all()
    context= {"rooms": rooms}
    return render(request,'rooms/home.html',context)

def room(request,pk):
    try:
        room= Room.objects.get(pk=pk)
        context= {"room": room}
        return render(request,'rooms/room.html',context)
    except Room.DoesNotExist:
        raise Http404