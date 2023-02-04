from django.shortcuts import render
from django.http import HttpResponse
from services.models import Service

# Create your views here.


def index(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'pages/index.html', context)


def services(request):
    return render(request, 'pages/services.html')


def about(request):
    return render(request, 'pages/about.html')


def gallery(request):
    return render(request, 'pages/gallery.html')


def contact(request):
    return render(request, 'pages/contact.html')
