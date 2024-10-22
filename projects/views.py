from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from .models import Project, Membership, FileUpload
from .forms import ProjectModelForm, FileUploadForm
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView,
    View
)


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectModelForm
    template_name = 'projects/project_create.html'
    success_url = reverse_lazy('projects:projects-list')

    def form_valid(self, form):
        # Save the project first
        project = form.save()
        # Save Team Leads
        team_leads = form.cleaned_data.get('team_leads')
        for lead in team_leads:
            Membership.objects.create(user=lead, project=project, role=Membership.TEAM_LEAD)

        # Save Team Members
        team_members = form.cleaned_data.get('team_members')
        for member in team_members:
            Membership.objects.create(user=member, project=project, role=Membership.TEAM_MEMBER)

            
        return super().form_valid(form)


class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    queryset = Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = self.get_queryset()
        user_projects = []

        for project in projects:
            is_team_member = project.is_team_member(self.request.user)
            is_team_lead = project.is_team_lead(self.request.user)
            user_projects.append((project, is_team_member, is_team_lead))

        context['user_projects'] = user_projects
        context['is_superuser'] = self.request.user.is_superuser

        return context


class ProjectDetailView(DetailView):
    template_name = 'projects/project_detail.html'
    queryset = Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()

        context['file_uploads'] = project.uploaded_files.all()
        context['team_leads'] = project.membership_set.filter(role=Membership.TEAM_LEAD)
        context['team_members'] = project.membership_set.filter(role=Membership.TEAM_MEMBER)
        context['is_team_member'] = project.is_team_member(self.request.user)
        context['is_superuser'] = self.request.user.is_superuser

        return context


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    form_class = ProjectModelForm
    success_url = reverse_lazy('projects:projects-list')

    def get_initial(self):
        initial = super().get_initial()
        project = self.object

        initial['team_leads'] = project.membership_set.filter(role=Membership.TEAM_LEAD).values_list('user', flat=True)
        initial['team_members'] = project.membership_set.filter(role=Membership.TEAM_MEMBER).values_list('user', flat=True)
        
        return initial

    def form_valid(self, form):
        project = form.save()
        Membership.objects.filter(project=project).delete()

        team_leads = form.cleaned_data.get('team_leads')
        for lead in team_leads:
            Membership.objects.create(user=lead, project=project, role=Membership.TEAM_LEAD)

        team_members = form.cleaned_data.get('team_members')
        for member in team_members:
            Membership.objects.create(user=member, project=project, role=Membership.TEAM_MEMBER)

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        context['file_uploads'] = project.uploaded_files.all()
        return context


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('projects:projects-list')


class FileUploadCreateView(CreateView):
    model = FileUpload
    form_class = FileUploadForm
    template_name = 'projects/file_upload.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs.get('project_id')
        context['project'] = get_object_or_404(Project, pk=project_id)
        return context

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        file_upload = form.save(commit=False)
        file_upload.project = project
        file_upload.save()
        return redirect('projects:projects-detail', pk=project.pk)


class FileUploadDeleteView(View):
    def post(self, request, pk):
        file_upload = get_object_or_404(FileUpload, pk=pk)
        project_id = file_upload.project.id
        file_upload.delete()
        return redirect(reverse('projects:projects-update', args=[project_id]))