from django.shortcuts import render, redirect

from .models import Incident
from .forms import *


# Create your views here.
def homepage(request):
    # Fetch all incidents from the database
    incidents = Incident.objects.all()  # You can filter if needed
    return render(request, 'homepage.html', {'incidents': incidents})

def my_events(request):
    return render(request, 'my_events.html')

def onaction(request):
    inc = Incident.objects.filter(status='On action')
    context = {'inc': inc}
    return render(request, 'onaction.html', context=context)

def noaction(request):
    inc = Incident.objects.filter(status='no action')
    context = {'inc': inc}
    return render(request, 'noaction.html', context)

def selectMode(request):
    return render(request, 'selectMode.html')

def about_us(request):
    return render(request, 'about_us.html')

def add_incident(request):
    form = IncidentForm()
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form': form}
    return render(request, template_name='add_incident.html', context=context)

def delete_incident(request, id):
    delete_inc = Incident.objects.get(pk=id)
    if request.method == 'POST':
        delete_inc.delete()
        return redirect('homepage')



def edit_incident(request, id):
    inc = Incident.objects.get(pk=id)
    form = IncidentForm(instance=inc)
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES, instance=inc)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, template_name='add_incident.html', context=context)