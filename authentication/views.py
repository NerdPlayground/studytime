from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

def register_study_time(request):
    form= UserCreationForm()
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
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

def logout_study_time(request):
    logout(request)
    return redirect('home')