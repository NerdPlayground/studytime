
from topics.models import Topic
from django.contrib import admin

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display= ["id","name"]
    search_fields= ["name"]