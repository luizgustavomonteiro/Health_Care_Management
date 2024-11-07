from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def patients(request):
    return render(request, 'patients.html', {})
