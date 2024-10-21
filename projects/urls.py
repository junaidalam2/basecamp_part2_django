from django.urls import path
from projects.views import (
    ProjectDetailView,
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
)

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='projects-detail'),
    path('create/', ProjectCreateView.as_view(), name='projects-create'),
    path('update/<int:pk>/', ProjectUpdateView.as_view(), name='projects-update'), 
    path('delete/<int:project_id>/', ProjectDeleteView.as_view(), name='projects-delete'), 
]
