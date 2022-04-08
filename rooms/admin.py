from rooms.models import Room
from django.contrib import admin

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display= ["host","topic","name","description"]
    search_fields= ["name"]
    list_filter= ["host","topic"]