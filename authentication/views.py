from rooms.models import Room
from topics.models import Topic
from django.http import Http404
from django.contrib import messages
from authentication.models import User
from django.shortcuts import render,redirect
from contributions.models import Contribution
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from authentication.forms import UpdateUserForm,RegisterUserForm

def register_study_time(request):
    form= RegisterUserForm()
    if request.method == 'POST':
        form= RegisterUserForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Warning: Failed to register user.')

    context= {"form":form}
    return render(request,'authentication/register.html',context)

def login_study_time(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Warning: User with provided credentials does not exist")

    context= {}
    return render(request,'authentication/login.html',context)

def profile(request,pk):
    try:
        user= User.objects.get(id=pk)
        topics= Topic.objects.all()
        rooms= Room.objects.filter(host=user)
        activities= Contribution.objects.filter(user=user)
        context= {
            "user": user,
            "topics": topics,
            "all_topics": topics.count(),
            "rooms": rooms,
            "activities": activities,
        }
        return render(request,'authentication/profile.html',context)
    except User.DoesNotExist:
        raise Http404

@login_required(login_url='login')
def update_profile(request):
    user= request.user
    form= UpdateUserForm(instance=user)

    if request.method == 'POST':
        form= UpdateUserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile',pk=user.id)

    context= {"form":form}
    return render(request,'authentication/update.html',context)

def logout_study_time(request):
    logout(request)
    return redirect('home')