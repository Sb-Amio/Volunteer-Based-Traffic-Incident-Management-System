from django.shortcuts import render, redirect

from Volunteer.models import Incident
from .forms import *


# Create your views here.
def homepage(request):
    # Fetch all incidents from the database
    incidents = Incident.objects.all()  # You can filter if needed
    return render(request, 'homepage.html', {'incidents': incidents})

def my_events(request):
    return render(request, 'my_events.html')

def onaction(request):
    return render(request, 'onaction.html')

def noaction(request):
    return render(request, 'noaction.html')

def selectMode(request):
    return render(request, 'selectMode.html')

def add_incident(request):
    form = IncidentForm()
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form': form}
    return render(request, template_name='add_incident.html', context=context)