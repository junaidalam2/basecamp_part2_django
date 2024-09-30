from django.urls import path
from projects.views import (
    ProjectDetailView,
    ProjectListView,
    ProjectCreateView
)

app_name = 'project'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
]
