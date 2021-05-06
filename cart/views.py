# Code adapted from the CI Boutique Ado mini project

from django.shortcuts import (
    render, redirect, reverse, HttpResponse)


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
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Store the shopping cart in the HTTP session
    cart = request.session.get('cart', {})

    """
    If a product with sizes is being added to the cart, then:
        if the same product id & size already exists, increase the quantity
        if the same product id exists, but has a new size, add the quantity
        Otherwise, add the new item and size to the cart
    Otherwise, add the product without a size to the cart
    """
    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
            else:
                cart[item_id]['items_by_size'][size] = quantity
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """
    Functionality for the update button in the shopping cart
    """

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Store the shopping cart in the HTTP session
    cart = request.session.get('cart', {})

    """
    If a product with sizes is being updated in the cart, then:
        if the updated qty is greater than zero, update the qty
        otherwise remove the item from the cart if qty is zero
    If a product without sizes is being updated in the cart, then:
        if the updated qty is greater than zero, update the qty
        otherwise remove the item from the cart if the qty is zero
    After the update, redirect back to the shopping cart page.
    """
    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    Functionality for the remove button in the shopping cart
    """
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        # Store the shopping cart in the HTTP session
        cart = request.session.get('cart', {})

        """
        If a product with sizes is being updated in the cart, then:
            if the updated qty is greater than zero, update the qty
            otherwise remove the item from the cart if qty is zero
        If a product without sizes is being updated in the cart, then:
            if the updated qty is greater than zero, update the qty
            otherwise remove the item from the cart if the qty is zero
        After the update, redirect back to the shopping cart page.
        """
        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
