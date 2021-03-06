import uuid
from django.db import models
from authentication.models import User

class Contribution(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user= models.ForeignKey(
        'authentication.User',
        related_name='contributions',
        on_delete=models.CASCADE
    )
    room= models.ForeignKey(
        'rooms.Room',
        related_name='contributions',
        on_delete=models.CASCADE
    )
    body= models.TextField()
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created','-updated')
    
    def __str__(self):
        return self.user.username +"'s contribution"