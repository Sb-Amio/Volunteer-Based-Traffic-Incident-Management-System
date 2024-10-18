from django.shortcuts import render

from Volunteer.models import Incident


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