from django.shortcuts import render, redirect, get_object_or_404
from summercamp.models import Camp
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.
@require_POST
def cart_add(request,camp_id):
    shopping_cart = Cart(request)
    camp = get_object_or_404(Camp,id=camp_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        shopping_cart.add(camp=camp,quantity=cd['quantity'],override_quantity=cd['override'])
    return redirect ('shopping_cart:cart_detail')  

def cart_remove(request, camp_id):
    shopping_cart = Cart(request)
    camp = get_object_or_404(Camp, id=camp_id)
    shopping_cart.remove(camp)  
    return redirect('shopping_cart:cart_detail')

def cart_detail(request):
    shopping_cart = Cart(request)
    return render(request, 'shopping_cart/cart_detail.html',{'shopping_cart':shopping_cart})