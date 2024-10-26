from django import forms
from .models import Thread, Message

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['message_text']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['topic']
        widgets = {
            'topic': forms.TextInput(attrs={
                'class': 'form-control',  # Bootstrap class for styling
                'placeholder': 'Topic',       # Placeholder for floating label
            }),
        }