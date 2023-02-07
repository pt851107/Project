from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('infantcare', views.infantcare, name='infantcare'),
    path('summercamp', views.summercamp, name='summercamp'),
    path('classes', views.classes, name='classes'),
    path('activities', views.activities, name='activities'),
    path('contact', views.contact, name='contact'),
    path('teachers', views.teachers, name='teachers'),
]
