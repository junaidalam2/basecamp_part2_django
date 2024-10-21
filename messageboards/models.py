from django.db import models
from projects.models import Project
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    project                     = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='messages')
    topic                       = models.CharField(max_length=255) 
    created_by                  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_messages')
    time_created                = models.DateTimeField(auto_now_add=True)
    time_updated                = models.DateTimeField(auto_now=True)
    last_updated_by             = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_messages')

    def __str__(self):
        return self.topic
    

class Thread(models.Model):
    message                     = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='threads')
    message_text                = models.TextField() 
    created_by                  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_threads')
    time_created                = models.DateTimeField(auto_now_add=True)
    time_updated                = models.DateTimeField(auto_now=True)
    last_updated_by             = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_threads')


    def __str__(self):
        return f'Thread in "{self.message.topic}" - {self.message_text[:30]}...'
    
