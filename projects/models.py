from django.db import models
from users.models import CustomUser


class Project(models.Model):
    name                        = models.CharField(max_length=255, blank=False, null=False) 
    description                 = models.TextField(blank=False, null=False)
    time_frame_for_completion   = models.DateField(blank=False, null=False)
    time_created                = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    time_updated = models.DateTimeField(auto_now=True, blank=False, null=False)
    users = models.ManyToManyField(CustomUser, related_name='projects', through='Membership')

    ACTIVE = 'A'
    COMPLETED = 'C'
    DORMANT = 'D'
    
    STATUS_CHOICES = (
        (ACTIVE, "Active"),
        (COMPLETED, "Completed"),
        (DORMANT, "Dormant"),
    )

    status = models.CharField(
        max_length=1, 
        choices = STATUS_CHOICES,
        default = ACTIVE,
    )

    
    def is_team_member(self, user):
        return self.membership_set.filter(user=user, role__in=['Team Member', 'Team Lead']).exists()

    
    def is_team_lead(self, user):
        return self.membership_set.filter(user=user, role=Membership.TEAM_LEAD).exists()
    
    def __str__(self):
        return self.name
    

class Membership(models.Model):
    TEAM_MEMBER = 'Team Member'
    TEAM_LEAD = 'Team Lead'
    
    ROLE_CHOICES = (
        (TEAM_MEMBER, 'Team Member'),
        (TEAM_LEAD, 'Team Lead'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=TEAM_MEMBER, blank=False, null=False)

    def __str__(self):
        return f"{self.user.email} - {self.role} in {self.project.name}"
    


class FileUpload(models.Model):
    project = models.ForeignKey(Project, related_name='uploaded_files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='project_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} uploaded for {self.project.name}"