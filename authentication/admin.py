from django.contrib import admin
from authentication.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ["username","first_name","last_name","email"]
    list_filter= ["is_active","is_staff"]
    search_fields= ["username","first_name","last_name"]