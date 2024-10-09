#from django.shortcuts import render
from django.urls import reverse_lazy
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
    success_url = reverse_lazy('projects:projects-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        print(self.success_url)
        return super().form_valid(form)
    

class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    queryset = Project.objects.all()


class ProjectDetailView(DetailView):
    template_name = 'projects/project_detail.html'
    queryset = Project.objects.all()


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    form_class = ProjectModelForm
    success_url = reverse_lazy('projects:projects-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        print(self.success_url)
        return super().form_valid(form)


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('projects:projects-list')
