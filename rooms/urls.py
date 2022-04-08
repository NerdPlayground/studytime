from django.urls import path
from rooms.views import room,home

urlpatterns= [
    path('',home,name="home"),
    path('',room,name="room"),
]