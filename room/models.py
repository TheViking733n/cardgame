from django.db import models

# Create your models here.

class Room(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    owner = models.EmailField()
    players = models.JSONField()
    config = models.JSONField()
    waiting = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

