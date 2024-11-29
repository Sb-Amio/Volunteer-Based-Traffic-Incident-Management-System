from django.db import models

# Create your models here.
from django.contrib.auth.models import User, AbstractUser


class Incident(models.Model):
    STATUS_CHOICES = [
        ('No Action', 'No Action'),
        ('On Action', 'On Action'),
        ('Completed', 'Completed'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='No Action')
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_incidents')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default= None,
                                    related_name='assigned_incidents')
    service_type = models.CharField(max_length=50,
                                    choices=[('Fire', 'Fire'), ('Police', 'Police'), ('Ambulance', 'Ambulance')],
                                    default='Police')
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_volunteer = models.BooleanField(default=False)

