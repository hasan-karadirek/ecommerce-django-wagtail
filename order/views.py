from django.shortcuts import render
from .utils import cartData

# Create your views here.
def checkout(request):
    data=cartData(request)
    cartItems=data["cartItems"]
    order=data["order"]
    items=data["items"]
    
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout1.html', context)
def cart(request):
    data=cartData(request)
    cartItems=data["cartItems"]
    order=data["order"]
    items=data["items"]
    
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'order/cart.html', context)