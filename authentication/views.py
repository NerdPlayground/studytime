from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

def access_study_time(request):
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
    return render(request,'authentication/access.html',context)

def leave_study_time(request):
    logout(request)
    return redirect('home')