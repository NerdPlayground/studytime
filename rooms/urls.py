from django.urls import path
from rooms.views import home,room,create_room,edit_room,delete_room

urlpatterns= [
    path('',home,name="home"),
    path('room/<str:pk>/',room,name="room"),
    path('create-room/',create_room,name="create-room"),
    path('edit-room/<str:pk>/',edit_room,name="edit-room"),
    path('delete-room/<str:pk>/',delete_room,name="delete-room"),
]