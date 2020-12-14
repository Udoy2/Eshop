from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    if cart:
        keys = list(cart.keys())
        items = list(cart.items())
        print(f"keys {items}")
        for id in keys:
            if int(id) == product.pk:
                return True

@register.filter(name='cart_count')
def cart_count(product,cart):
    if cart:
        keys = list(cart.keys())
        print(f"keys {keys}")
        for id in keys:
            if int(id) == product.pk:
                return cart.get(id)
