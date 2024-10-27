from django.forms import ModelForm
from .models import *

class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = '__all__'
