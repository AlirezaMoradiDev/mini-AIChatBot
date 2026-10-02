from django.contrib.auth.models import User
from django.db import models

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    class CreatorType(models.TextChoices):
        BOT = 'bot'
        USER = 'user'
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=6, choices=CreatorType.choices)
