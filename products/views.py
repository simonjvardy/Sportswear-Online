from django.shortcuts import render
from .models import Product

"""
Adapted from Code Institute Boutique Ado mini project
"""



def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
