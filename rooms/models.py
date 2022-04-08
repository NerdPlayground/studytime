from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    host= models.ForeignKey(
        'auth.User',
        related_name='rooms',
        on_delete=models.CASCADE
    )
    topic= models.ForeignKey(
        'topics.Topic',
        related_name='rooms',
        on_delete=models.CASCADE
    )
    name= models.CharField(max_length=255)
    description= models.TextField()
    # Participants= models.
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)