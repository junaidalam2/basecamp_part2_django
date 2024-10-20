from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Message, Thread
from .forms import ThreadForm
from projects.models import Project
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)


class MessageCreateView(CreateView):
    model = Message
    fields = ['topic']
    template_name = 'messageboards/message_create.html'

    def get_success_url(self):
        return reverse_lazy('messageboards:project-messageboard-list', kwargs={'project_id': self.kwargs['project_id']})

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        form.instance.project = project
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ThreadCreateView(CreateView):
    model = Thread
    fields = ['message_text']
    template_name = 'messageboards/thread_create.html'
    success_url = reverse_lazy('projects:projects-list')

    def form_valid(self, form):
        message = get_object_or_404(Message, pk=self.kwargs['message_id'])
        form.instance.message = message
        form.instance.created_by = self.request.user
        form.save()
        return redirect('messageboards:project-messageboard-list', project_id=message.project.id)


class MessageboardListView(ListView):
    model = Message
    template_name = 'messageboards/project_messageboard_list.html'
    context_object_name = 'message_list'

    def get_queryset(self):
        project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        return Message.objects.filter(project=project).prefetch_related('threads')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs['project_id'])
        context['thread_form'] = ThreadForm() 
        return context