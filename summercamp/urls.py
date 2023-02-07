from django.urls import path
from . import views

app_name = 'summercamp'

urlpatterns = [
    path('', views.index, name='summercamp'),
    path('', views.product_list, name = 'product_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail') 
]
