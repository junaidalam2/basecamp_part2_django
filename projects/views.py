from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Project
from .forms import ProjectModelForm
# Create your views here.

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

class ProjectCreateView(CreateView):
    template_name = 'projects/project_create.html'
    form_class = ProjectModelForm
    queryset = Project.objects.all() 
    success_url = reverse_lazy('project-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    queryset = Project.objects.all()


class ProjectDetailView(DetailView):
    template_name = 'projects/project_detail.html'
    queryset = Project.objects.all()