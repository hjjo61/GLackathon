from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'patients/dashboard.html')

def patientqueue(request):
    return render(request, 'patients/patientqueue.html')

def administration(request):
    return render(request, 'patients/administration.html')