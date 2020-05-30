from django.conf import settings
from django.db import models

# Create your models here.

class ChatMessage(models.Model):
    username = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    def __str__(self):
        return self.username