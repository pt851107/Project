from django.shortcuts import render
from .models import Gallery

# Create your views here.


def index(request):
    gallerys = Gallery.objects.all()
    context = {'gallerys': gallerys}
    return render(request, 'pages/gallery.html', context)
