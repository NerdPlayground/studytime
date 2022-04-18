from django.forms import ModelForm
from authentication.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    class Meta:
        model= User
        fields= [
            "username","email",
            "password1","password2"
        ]

class UpdateUserForm(ModelForm):
    class Meta:
        model= User
        fields= [
            'avatar','username',
            'first_name','last_name',
            'email','description'
        ]