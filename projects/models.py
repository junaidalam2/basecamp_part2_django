from django.db import models
from users.models import CustomUser


class Project(models.Model):
    name                        = models.CharField(max_length=255) 
    description                 = models.TextField()
    time_frame_for_completion   = models.DateField()
    time_created                = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
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
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=TEAM_MEMBER)

    def __str__(self):
        return f"{self.user.email} - {self.role} in {self.project.name}"