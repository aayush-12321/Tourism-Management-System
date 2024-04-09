#filters

from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(package  , cart):
    keys = cart.keys()
    # print(package)
    for id in keys:
        if int(id) == package.id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(package  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == package.id:
            return cart.get(id)
    return 0


@register.filter(name='price_total')
def price_total(package  , cart):
    return package.price * cart_quantity(package , cart)


@register.filter(name='total_cart_price')
def total_cart_price(packages , cart):
    sum = 0 
    for p in packages:
        sum += price_total(p , cart)

    return sum
    