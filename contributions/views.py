from django.http import Http404,HttpResponse
from django.shortcuts import render,redirect
from contributions.models import Contribution
from django.contrib.auth.decorators import login_required

def all_activities(request):
    activities= Contribution.objects.all()
    context= {"activities":activities}
    return render(request,'contributions/activities.html',context)

@login_required(login_url='login')
def delete_contribution(request,pk):
    try:
        contribution= Contribution.objects.get(id=pk)

        if request.user != contribution.user:
            return HttpResponse("Warning: Current user and host don't match.")
            
        if request.method == 'POST':
            contribution.delete()
            return redirect('room',pk=contribution.room.id)
        
        return render(request,'delete.html',{'obj':contribution})
    except Contribution.DoesNotExist:
        raise Http404