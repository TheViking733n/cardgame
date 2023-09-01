from django.db import models

# Create your models here.

class Room(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    creator = models.EmailField()
    players = models.JSONField()
    lastSeen = models.JSONField()
    config = models.JSONField()
    waiting = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Room {self.id} created by {self.creator} at {self.created_at}"