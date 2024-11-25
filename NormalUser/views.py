from datetime import timedelta
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from Volunteer.forms import UserProfileForm
from Volunteer.models import Incident


# Create your views here.
@login_required
def homepage_volunteer(request):
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

@login_required
def assign_volunteer(request, id):
    incident = get_object_or_404(Incident, id=id)
    incident.assigned_to = request.user
    incident.status = 'On Action'
    incident.save()
    return redirect('on_action_vol')

@login_required
def unassign_volunteer(request, id):
    incident = get_object_or_404(Incident, id=id)
    incident.assigned_to = None
    incident.status = 'No Action'
    incident.save()
    return redirect('no_action_vol')

@login_required
def complete_volunteer(request, id):
    incident = get_object_or_404(Incident, id=id)
    incident.status = 'Completed'
    incident.save()
    return redirect('completed_vol')

def logout_volunteer(request):
    logout(request)  # Log the user out
    return redirect('login_page')

@login_required
def search_events_volunteer(request):
    query = request.GET.get('query', '').strip()  # Strip any extra whitespace from the query
    search_results = []

    if query:
        # Filter incidents based on location with case-insensitive and partial matching
        search_results = Incident.objects.filter(location__icontains=query)

    context = {'search_results': search_results, 'query': query}
    return render(request, 'search_results_vol.html', context=context)

@login_required
def event_details_volunteer(request, id):
    incident = get_object_or_404(Incident, id=id)
    context = {'incident': incident}
    return render(request, 'event_details_vol.html', context)

@login_required
def profile_view_volunteer(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')  # Add success message
            return redirect('profile_vol')  # Redirect after saving
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = UserProfileForm(instance=user)

    context = {'form': form}
    return render(request, 'profile_vol.html', context=context)

@login_required
def my_involvements(request):
    inc = Incident.objects.filter(assigned_to=request.user).order_by('-date_reported')
    context = {'inc': inc}
    return render(request, template_name='my_involvements.html', context=context)

@login_required
def on_action_volunteer(request):
    inc = Incident.objects.filter(status='On Action').order_by('-date_reported')
    context = {'inc': inc}
    return render(request, 'on_action_vol.html', context=context)
@login_required
def no_action_volunteer(request):
    inc = Incident.objects.filter(status='No Action').order_by('-date_reported')
    context = {'inc': inc}
    return render(request, 'no_action_vol.html', context)

@login_required
def completed_volunteer(request):
    inc = Incident.objects.filter(status='Completed').order_by('-date_reported')
    context = {'inc': inc}
    return render(request, 'complete_vol.html', context)