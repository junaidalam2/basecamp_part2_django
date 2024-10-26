from django import forms
from .models import Project, CustomUser, FileUpload
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
        # to enable floating labels in bootstrap
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'id_description', 'rows': 4}),
            'time_frame_for_completion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'id_time_frame_for_completion'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.required:
                field.label += ' *'

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


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'inputGroupFile04'}),
        }