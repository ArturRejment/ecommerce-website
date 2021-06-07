import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        
    items = []
    order = {'get_cart_total':0, 'get_cart_items':0}
    cartItems = order["get_cart_items"]

    for item in cart:
        try:
            cartItems += cart[item]['quantity']
            
            product = Product.objects.get(id = item)
            total = (product.price * cart[item]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[item]['quantity']

            cart_item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },
                'quantity': cart[item]['quantity'],
                'get_total': total
            }
            items.append(cart_item)
            
            if product.digital == False:
                order['shipping'] = True
        except:
            pass
    return {'cartItems': cartItems, 'order': order, 'items':items}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        shipping = order.shipping
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
        shipping = order['shipping']
    
    return {'items': items, 'order': order, 'cartItems': cartItems, 'shipping': shipping}
