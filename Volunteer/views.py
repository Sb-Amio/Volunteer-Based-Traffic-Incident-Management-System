from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Incident
from .forms import *

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')  # Redirect to a success page
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomLoginForm()
    return render(request, 'login_page.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            return redirect('login_page')  # Redirect to the login page after successful registration
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
    inc = Incident.objects.filter(status='on action')
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
            form.instance.reported_by = request.user
            form.save()
            return redirect('homepage')
    else:
        # Set initial 'reported_by' field value for GET request (form display)
        form = IncidentForm(initial={'reported_by': request.user.username})

    context = {'form': form}
    return render(request, template_name='add_incident.html', context=context)

def delete_incident(request, id):

    incident = Incident.objects.get(id=id)
    if request.method == 'POST':
        incident.delete()  # Delete the incident
        return redirect('homepage')
    return render(request, template_name='confirm_delete.html')

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


