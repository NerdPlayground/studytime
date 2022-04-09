from rooms.models import Room
from django.db.models import Q
from topics.models import Topic
from django.http import Http404
from rooms.forms import RoomForm
from django.shortcuts import render,redirect

def home(request):
    query= request.GET.get('query') if request.GET.get('query') != None else ''
    rooms= Room.objects.filter(
        Q(topic__name__icontains=query) |
        Q(name__icontains=query) |
        Q(description__icontains=query)
    )
    topics= Topic.objects.all()
    context= {"rooms":rooms,"topics":topics,"room_count":rooms.count()}
    return render(request,'rooms/home.html',context)

def room(request,pk):
    try:
        room= Room.objects.get(pk=pk)
        context= {"room":room}
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
    
    context= {"form":form}
    return render(request,'rooms/room_form.html',context)

def edit_room(request,pk):
    try:
        room= Room.objects.get(id=pk)
        form= RoomForm(instance=room)

        if request.method == 'POST':
            form= RoomForm(request.POST,instance=room)
            if form.is_valid():
                form.save()
                return redirect('home')

        context= {"form":form}
        return render(request,'rooms/room_form.html',context)
    except Room.DoesNotExist:
        raise Http404

def delete_room(request,pk):
    try:
        room= Room.objects.get(id=pk)
        if request.method == 'POST':
            room.delete()
            return redirect('home')
        return render(request,'delete.html',{'obj':room})
    except Room.DoesNotExist:
        raise Http404