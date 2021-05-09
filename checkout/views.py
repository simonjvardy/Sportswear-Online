# Code adapted from CI Boutique Ado mini projects

from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from cart.contexts import cart_contents
import stripe


def checkout(request):
    """
    Take the order and user details from the checkout form
    and create the order in the dataabase
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'telephone': request.POST['telephone'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)

        """
        For each item in the cart, create an order line item
        checking whether the product has a size or not.
        On the rare occassion that the product doesn't exist in the database
        delete the order and return the user to the shopping cart page
        """
        if order_form.is_valid():
            order_form.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request,
                "There's nothing in you shopping cart at the moment!"
            )
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']

        # stripe requires the value as an integer as a zero-decimal currency
        # e.g. £4.99 = 499p
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key missing. Please set it in your environment.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # if request.user.is_authenticated:
    #     profile = UserProfile.objects.get(user=request.user)
    #     # Attach the user's profile to the order
    #     order.user_profile = profile
    #     order.save()

        # Save the user's info
        # if save_info:
        #     profile_data = {
        #         'default_telephone': order.telephone,
        #         'default_country': order.country,
        #         'default_postcode': order.postcode,
        #         'default_town_or_city': order.town_or_city,
        #         'default_address_line1': order.address_line1,
        #         'default_address_line2': order.address_line2,
        #         'default_county': order.county,
        #     }
        #     user_profile_form = UserProfileForm(profile_data, instance=profile)
        #     if user_profile_form.is_valid():
        #         user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)