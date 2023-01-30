from django.shortcuts import render,redirect
from django.contrib import messages

def contact(request):
    return render(request, 'pages/contact.html')
