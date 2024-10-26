from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Message, Thread
from .forms import ThreadForm,  MessageForm
from projects.models import Project
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView
)


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'messageboards/message_create.html'

    def get_success_url(self):
        return reverse_lazy('messageboards:project-messageboard-list', kwargs={'project_id': self.kwargs['project_id']})

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        form.instance.project = project
        form.instance.created_by = self.request.user
        form.instance.last_updated_by = self.request.user
        return super().form_valid(form)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        topic_field = self.form_class.base_fields.get('topic')
        if topic_field and topic_field.required:
            topic_field.label += ' *'

class ThreadCreateView(CreateView):
    model = Thread
    fields = ['message_text']
    template_name = 'messageboards/thread_create.html'
    success_url = reverse_lazy('projects:projects-list')

    def form_valid(self, form):
        message = get_object_or_404(Message, pk=self.kwargs['message_id'])
        form.instance.message = message
        form.instance.created_by = self.request.user
        form.instance.last_updated_by = self.request.user
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
        project = Project.objects.get(id=self.kwargs['project_id'])
        context['project'] = project
        context['thread_form'] = ThreadForm()
        context['is_team_member'] = project.is_team_member(self.request.user)
        context['is_team_lead'] = project.is_team_lead(self.request.user)
        context['is_superuser'] = self.request.user.is_superuser
        context['tooltip_text_team_lead'] = "Topics can only be created, edited and deleted by Team Leads."
        context['tooltip_text_team_member'] = "Messages can only be created, edited and deleted by members of the project team."
        
        return context
    

class ThreadDeleteView(DeleteView):
    model = Thread
    #template_name = 'messageboards/thread_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('messageboards:project-messageboard-list', kwargs={'project_id': self.object.message.project.id})


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['topic']

    def form_valid(self, form):
        form.instance.last_updated_by = self.request.user
        return super().form_valid(form)


# class ThreadUpdateView(UpdateView):
#     model = Thread
#     fields = ['message_text']

#     def form_valid(self, form):
#         form.instance.last_updated_by = self.request.user
#         return super().form_valid(form)

class MessageEditView(UpdateView):
    model = Message
    fields = ['topic']

    def get_success_url(self):
        return reverse_lazy('messageboards:project-messageboard-list', kwargs={'project_id': self.object.project.id})


class ThreadUpdateView(UpdateView):
    model = Thread
    fields = ['message_text']
    template_name = 'messageboards/project_messageboard_list.html'

    def get_success_url(self):
        message = self.object.message
        return reverse_lazy('messageboards:project-messageboard-list', kwargs={'project_id': message.project.pk})

    def form_valid(self, form):
        form.instance.last_updated_by = self.request.user
        return super().form_valid(form)
    

class MessageDeleteView(DeleteView):
    model = Message
    
    def get_success_url(self):
        message = self.get_object()
        return reverse_lazy('messageboards:project-messageboard-list', kwargs={'project_id': message.project.id})
