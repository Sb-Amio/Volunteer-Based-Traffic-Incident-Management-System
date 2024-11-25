from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Corrected attribute access for UserProfile
                if hasattr(user, 'userprofile') and user.userprofile.is_volunteer:
                    return redirect('homepage_vol')  # Redirect to volunteer dashboard
                else:
                    return redirect('homepage')  # Redirect to normal user dashboard
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login_page.html', {'form': form})

def sign_up(request, user_type):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a UserProfile instance associated with the user
            is_volunteer = True if user_type == 'Volunteer' else False
            UserProfile.objects.create(user=user, is_volunteer=is_volunteer)
            return redirect('login_page')
    else:
        form = RegistrationForm()
    return render(request, 'signup_page.html', {'form': form})

def logout_view(request):
    logout(request)  # Log the user out
    return redirect('login_page')  # Redirect to the login page after logout
@login_required
def homepage(request):
    incidents = Incident.objects.all().order_by('-date_reported')  # Order by newest first
    current_time = timezone.now()
    # Annotate each incident with 'is_new' flag
    for incident in incidents:
        time_difference = current_time - incident.date_reported
        incident.is_new = time_difference <= timedelta(hours=1)  # Flag if within the last hour
    context = {'incidents': incidents}
    return render(request, 'homepage.html', context=context)

@login_required
def my_events(request):
    inc = Incident.objects.filter(reported_by=request.user).order_by('-date_reported')
    context = {'inc': inc}
    return render(request, template_name='my_events.html', context=context)

def onaction(request):
    inc = Incident.objects.filter(status='On Action').order_by('-date_reported')
    context = {'inc': inc}
    return render(request, 'onaction.html', context=context)

def noaction(request):
    inc = Incident.objects.filter(status='No Action').order_by('-date_reported')
    context = {'inc': inc}
    return render(request, 'noaction.html', context)

def completed(request):
    inc = Incident.objects.filter(status='Completed').order_by('-date_reported')
    context = {'inc': inc}
    return render(request, 'complete.html', context)

def selectMode(request):
    return render(request, 'selectMode.html')

def about_us(request):
    return render(request, 'about_us.html')

@login_required
def add_incident(request):
    form = IncidentForm()
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.reported_by = request.user
            form.save()
            return redirect('homepage')
    else:
        # Set initial 'reported_by' field value for GET request (form display)
        form = IncidentForm(initial={'reported_by': request.user.username})

    context = {'form': form}
    return render(request, template_name='add_incident.html', context=context)

@login_required
def delete_incident(request, id):
    incident = Incident.objects.get(id=id)
    if request.method == 'POST':
        incident.delete()  # Delete the incident
        return redirect('my_eventss')
    return render(request, template_name='confirm_delete.html')

@login_required
def edit_incident(request, id):
    inc = Incident.objects.get(pk=id)
    form = IncidentForm(instance=inc)
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES, instance=inc)
        if form.is_valid():
            form.save()
            return redirect('my_events')
    context = {'form': form}
    return render(request, template_name='add_incident.html', context=context)

@login_required
def search_events(request):
    query = request.GET.get('query', '').strip()  # Strip any extra whitespace from the query
    search_results = []

    if query:
        # Filter incidents based on location with case-insensitive and partial matching
        search_results = Incident.objects.filter(location__icontains=query)

    context = {'search_results': search_results, 'query': query}
    return render(request, 'search_results.html', context=context)


@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')  # Add success message
            return redirect('profile')  # Redirect after saving
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = UserProfileForm(instance=user)

    context = {'form': form}
    return render(request, 'profile.html', context=context)


@login_required
def event_details(request, id):
    incident = get_object_or_404(Incident, id=id)
    context = {'incident': incident}
    return render(request, 'event_details.html', context)

