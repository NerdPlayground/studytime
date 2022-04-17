import uuid
from django.db import models
from authentication.models import User

class Room(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    host= models.ForeignKey(
        'authentication.User',
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
    participants= models.ManyToManyField(
        'authentication.User',
        related_name='contributors',
        blank=True
    )
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created','-updated')

    def __str__(self):
        return self.name