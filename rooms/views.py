from rooms.models import Room
from django.http import Http404
from rooms.forms import RoomForm
from django.shortcuts import render,redirect

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

def create_room(request):
    form= RoomForm()

    if request.method == 'POST':
        form= RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context= {'form': form}
    return render(request,'rooms/room_form.html',context)
    