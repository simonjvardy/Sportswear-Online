# Code adapted from the CI Boutique Ado mini project

from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """
    This view returns the shopping cart contents page
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add the item & quantity to the shopping cart
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # Store the shopping cart in the HTTP session
    cart = request.session.get('cart', {})
    
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
