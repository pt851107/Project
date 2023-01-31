from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')

def services(request):
    return render(request, 'services/services.html')

def pricing(request):
    return render(request, 'pages/pricing.html')

def about(request):
    return render(request, 'pages/about.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def contact(request):
    return render(request, 'pages/contact.html')
