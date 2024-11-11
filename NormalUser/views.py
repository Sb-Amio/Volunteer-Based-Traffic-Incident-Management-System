from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from Volunteer.models import Incident


# Create your views here.
@login_required
def homepage(request):
    incidents = Incident.objects.all().order_by('-date_reported')  # Order by newest first
    current_time = timezone.now()
    # Annotate each incident with 'is_new' flag
    for incident in incidents:
        time_difference = current_time - incident.date_reported
        incident.is_new = time_difference <= timedelta(hours=1)  # Flag if within the last hour
    context = {'incidents': incidents}
    return render(request, 'homepage_vol.html', context=context)

@login_required
def about_us_volunteer(request):
    return render(request, 'about_us_vol.html')