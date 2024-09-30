from django import forms

from .models import Project

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'time_frame_for_completion',
        ]