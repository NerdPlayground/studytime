from rooms.models import Room
from django.db.models import Q
from topics.models import Topic
from rooms.forms import RoomForm
from django.http import Http404,HttpResponse
from django.shortcuts import render,redirect
from contributions.models import Contribution
from django.contrib.auth.decorators import login_required

def home(request):
    query= request.GET.get('query') if request.GET.get('query') != None else ''
    rooms= Room.objects.filter(
        Q(topic__name__icontains=query) |
        Q(name__icontains=query) |
        Q(description__icontains=query)
    )
    topics= Topic.objects.all()

    activities= Contribution.objects.filter(
        Q(room__topic__name__icontains=query)
    )
    context= {
        "rooms":rooms,
        "topics":topics[0:5],
        "all_topics":topics.count(),
        "activities":activities,
        "room_count":rooms.count()
    }
    return render(request,'rooms/home.html',context)

def room(request,pk):
    try:
        room= Room.objects.get(id=pk)
        contributions= Contribution.objects.filter(room=room)

        if request.method == 'POST':
            contribution= Contribution.objects.create(
                user= request.user,
                room= room,
                body= request.POST.get('body')
            )
            contribution.save()
            room.participants.add(request.user)
            return redirect('room',pk=room.id)

        context= {
            "room":room,
            "contributions":contributions,
            "contributors": room.participants.all()
        }
        return render(request,'rooms/room.html',context)
    except Room.DoesNotExist:
        raise Http404

@login_required(login_url='login')
def create_room(request):
    form= RoomForm()
    topics= Topic.objects.all()

    if request.method == 'POST':
        topic,created= Topic.objects.get_or_create(
            name=request.POST.get('topic')
        )
        Room.objects.create(
            host= request.user,
            topic= topic,
            name= request.POST.get('name'),
            description= request.POST.get('description')
        )
        return redirect('home')
    
    context= {"form":form,"topics":topics}
    return render(request,'rooms/room_form.html',context)

@login_required(login_url='login')
def edit_room(request,pk):
    try:
        topics= Topic.objects.all()
        room= Room.objects.get(id=pk)
        form= RoomForm(instance=room)

        if request.user != room.host:
            return HttpResponse("Warning: Current user and host don't match.")
        
        if request.method == 'POST':
            topic,created= Topic.objects.get_or_create(
                name=request.POST.get('topic')
            )
            room.topic= topic
            room.name= request.POST.get('name')
            room.description= request.POST.get('description')
            room.save()
            return redirect('home')

        context= {
            "form":form,
            "room":room,
            "topics":topics
        }
        return render(request,'rooms/room_form.html',context)
    except Room.DoesNotExist:
        raise Http404

@login_required(login_url='login')
def delete_room(request,pk):
    try:
        room= Room.objects.get(id=pk)

        if request.user != room.host:
            return HttpResponse("Warning: Current user and host don't match.")
            
        if request.method == 'POST':
            room.delete()
            return redirect('home')
        return render(request,'delete.html',{'obj':room})
    except Room.DoesNotExist:
        raise Http404