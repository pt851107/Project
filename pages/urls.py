from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('pricing', views.pricing, name='pricing'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact')
]
