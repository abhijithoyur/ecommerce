from .models import Cart,CartItem
from .views import cart__id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=cart__id(request))
            car_items=CartItem.objects.all().filter(cart=cart[:1])
            for i in car_items:
                item_count += i.quantity
        except Cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)