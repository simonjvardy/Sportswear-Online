"""
Code adapted from the CI Boutique Ado mini project
"""
from django import template


register = template.Library()


@register.filter(name='calculate_subtotal')
def calculate_subtotal(discount_price, quantity):
    return discount_price * quantity
