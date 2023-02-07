from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def index(request):
    summercamp = Product.objects.all()
    context = {'summercamp':summercamp}
    return render(request,'summercamp/summercamp.html',context)

def product_list(request):
    products = Product.objects.filter(available = True)
    return render(request, 'summercamp/summercamp.html', {'products':products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'summercamp/detail.html',{'product':product})