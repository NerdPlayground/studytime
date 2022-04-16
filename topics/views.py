from topics.models import Topic
from django.http import Http404,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

def topics(request):
    topics= Topic.objects.all()
    query= request.GET.get('query') if request.GET.get('query') != None else ''
    context= {
        "all_topics": topics.count(),
        "topics":topics.filter(name__icontains=query),
    }
    return render(request,'topics/topics.html',context)