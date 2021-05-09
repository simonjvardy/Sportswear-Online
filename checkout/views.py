# Code adapted from CI Boutique Ado mini projects

from django.shortcuts import (
    render, redirect, reverse)
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(
            request,
            "There's nothing in you shopping cart at the moment!"
        )
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IcvcUHJhe50oHXbOfXzaUFdrGPP9kotW4kN7g3vPWPVvQRRefjPAujUlGcYHO3UZydz8I56L0i98jxID1pm51vl00uwbspCEF',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
