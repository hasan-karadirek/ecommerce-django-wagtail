import json
from .models import Order
from product.models import Product

def cookieCart(request):
    
    try:
        cart = json.loads(request.COOKIES['cart'])
        
    except:
        cart = {}
    items=[]
    order = {'get_cart_total':0, 'get_cart_items':0, "shipping":False,}
    cartItems=order['get_cart_items']
    
    for i in cart:
        
        print("try")
        print(cart[i])
        cartItems+=cart[i]['quantity']
        
        product = Product.objects.get(id=i)
        
        total = (product.current_price * cart[i]['quantity'])
        
        order['get_cart_total'] += total
        order['get_cart_items'] += cart[i]['quantity']
        
        item = {
            'id':product.id,
            'product':{'id':product.id,'name':product.name, 'price':product.current_price,
            'image':product.image}, 'quantity':cart[i]['quantity'],
            'get_total':total,
        }
        print('hata')
        items.append(item)
        
    print(items)
    return {'cartItems':cartItems ,'order':order, 'items':items}
def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        cookieData=cookieCart(request)
        cartItems=cookieData["cartItems"]
        order=cookieData["order"]
        items=cookieData["items"]
    return {'cartItems':cartItems ,'order':order, 'items':items}
def newfunc(asd):
    pass