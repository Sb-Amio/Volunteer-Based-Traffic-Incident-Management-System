from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def my_events(request):
    return render(request, 'my_events.html')

def onaction(request):
    return render(request, 'onaction.html')

def noaction(request):
    return render(request, 'noaction.html')