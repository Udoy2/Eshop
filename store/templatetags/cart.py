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
@register.filter(name='total_product_price')
def total_product_price(product,cart):
    return  product.price * cart_count(product,cart)

@register.filter(name='total_price')
def total_cart_price(products,cart):
    sum = 0
    for product in products:
        sum += total_product_price(product,cart)
    return sum
