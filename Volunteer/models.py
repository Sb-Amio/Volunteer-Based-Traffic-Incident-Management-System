from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Incident(models.Model):
    STATUS_CHOICES = [
        ('no action', 'no action'),
        ('on action', 'On action'),
        ('completed', 'completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='no action')
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_incidents')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='assigned_incidents')
    service_type = models.CharField(max_length=50,
                                    choices=[('fire', 'Fire'), ('police', 'Police'), ('ambulance', 'Ambulance')],
                                    default='police')
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username