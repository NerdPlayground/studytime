from dataclasses import fields
from django.forms import ModelForm
from authentication.models import User

class UserForm(ModelForm):
    class Meta:
        model= User
        fields= ['username','first_name','last_name','email']