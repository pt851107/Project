from django.shortcuts import render
from django.http import HttpResponse
from teachers.models import Teacher
from gallerys.models import Gallery
from summercamp.models import Camp

# Create your views here.


def index(request):
    teachers = Teacher.objects.all()
    gallerys = Gallery.objects.all()
    summercamp = Camp.objects.all()
    context = {
        'teachers': teachers,
        'gallerys': gallerys,
        'summercamp': summercamp
    }
    return render(request, 'pages/index.html', context)


def infantcare(request):
    return render(request, 'pages/infantcare.html')


def summercamp(request):
    summercamp = Camp.objects.all()
    context = {
        'summercamp': summercamp
    }
    return render(request, 'summercamp/summercamp.html', context)


def classes(request):
    return render(request, 'pages/classes.html')


def activities(request):
    return render(request, 'pages/activities.html')


def contact(request):
    return render(request, 'pages/contact.html')


def teachers(request):
    return render(request, 'pages/teachers.html')
