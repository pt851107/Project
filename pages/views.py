from django.shortcuts import render
from django.http import HttpResponse
from services.models import Service
from teachers.models import Teacher

# Create your views here.


def index(request):
    services = Service.objects.all()
    teachers = Teacher.objects.all()
    context = {
        'services': services,
        'teachers': teachers,
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


def loginPage(request):
    context = {}
    return render(request, 'pages/login_register.html', context)
