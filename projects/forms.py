from django import forms
from .models import Project, CustomUser
from django.core.exceptions import ValidationError

class ProjectModelForm(forms.ModelForm):

    team_members = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Team Members"
    )

    team_leads = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple,
        label="Team Leads"
    )

    status = forms.ChoiceField(
         choices=Project.STATUS_CHOICES,
         initial=Project.ACTIVE,
         label='Project Status'
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'time_frame_for_completion', 'status']


    def clean(self):
            cleaned_data = super().clean()
            team_leads = cleaned_data.get('team_leads')
            team_members = cleaned_data.get('team_members')

            if not team_leads:
                raise ValidationError('At least one user must be assigned as a Team Lead.')

            if team_leads and team_members:
                overlap = set(team_leads) & set(team_members)
                if overlap:
                    raise ValidationError('A user cannot be both a Team Lead and a Team Member.')

            return cleaned_data