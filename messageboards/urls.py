from django.urls import path
from .views import (
    MessageCreateView, 
    ThreadCreateView,
    MessageboardListView,
    ThreadDeleteView,
    ThreadUpdateView,
    MessageDeleteView,
    MessageEditView,
)

app_name = 'messageboards'

urlpatterns = [
    path('projects/<int:project_id>/message/new/', MessageCreateView.as_view(), name='message-create'),
    path('projects/<int:project_id>/', MessageboardListView.as_view(), name='project-messageboard-list'),
    path('messages/<int:message_id>/thread/new/', ThreadCreateView.as_view(), name='thread-create'),
    path('threads/<int:pk>/delete/', ThreadDeleteView.as_view(), name='thread-delete'),
    path('threads/<int:pk>/edit/', ThreadUpdateView.as_view(), name='thread-edit'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message-delete'),
    path('message/edit/<int:pk>/', MessageEditView.as_view(), name='message-edit'),
]
