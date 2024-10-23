from django.urls import path
from projects.views import (
    ProjectDetailView,
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    FileUploadCreateView,
    FileUploadDeleteView,
)

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='projects-detail'),
    path('create/', ProjectCreateView.as_view(), name='projects-create'),
    path('update/<int:pk>/', ProjectUpdateView.as_view(), name='projects-update'), 
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='projects-delete'),
    path('project/<int:project_id>/upload/', FileUploadCreateView.as_view(), name='upload_file'),
    path('file_upload/delete/<int:pk>/', FileUploadDeleteView.as_view(), name='file_upload_delete'),
]
