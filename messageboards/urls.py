from django.urls import path
from .views import (
    MessageCreateView, 
    ThreadCreateView,
    MessageboardListView,
)

app_name = 'messageboards'

urlpatterns = [
    path('projects/<int:project_id>/message/new/', MessageCreateView.as_view(), name='message-create'),
    path('projects/<int:project_id>/', MessageboardListView.as_view(), name='project-messageboard-list'),
    path('messages/<int:message_id>/thread/new/', ThreadCreateView.as_view(), name='thread-create'),
]
