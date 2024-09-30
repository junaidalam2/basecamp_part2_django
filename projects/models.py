from django.db import models
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    name                        = models.CharField(max_length=255) 
    description                 = models.TextField()
    time_frame_for_completion   = models.DateField()
    time_created                = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True) 

    def save(self, *args, **kwargs):
        if not self.time_frame_for_completion:
            self.time_frame_for_completion = timezone.now()
        super(Project, self).save(*args, **kwargs)
    
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

    
