from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from django.db.models import Q
from .models import (
    Product, Gender, MasterCategory, SubCategory, ArticleType)


"""
Adapted from Code Institute Boutique Ado mini project
"""


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all()
    query = None
    gender = None
    master_category = None
    sub_category = None
    article_type = None

    if request.GET:
        if 'gender' in request.GET:
            gender = request.GET['gender'].split(',')
            products = products.filter(gender__name__in=gender)
            gender = Gender.objects.filter(name__in=gender)

        if 'master_category' in request.GET:
            master_category = request.GET['master_category'].split(',')
            products = products.filter(master_category__name__in=master_category)
            master_category = MasterCategory.objects.filter(
                name__in=master_category)

        if 'sub_category' in request.GET:
            sub_category = request.GET['sub_category'].split(',')
            products = products.filter(sub_category__name__in=sub_category)
            sub_category = SubCategory.objects.filter(name__in=sub_category)

        if 'article_type' in request.GET:
            article_type = request.GET['article_type'].split(',')
            products = products.filter(article_type__name__in=article_type)
            article_type = ArticleType.objects.filter(name__in=article_type)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a seearch criteria")
                return redirect(reverse('products'))
            
            queries = (
                Q(name__icontains=query) |
                Q(product_description__icontains=query) |
                Q(gender__name__icontains=query) |
                Q(master_category__name__icontains=query) |
                Q(sub_category__name__icontains=query) |
                Q(article_type__name__icontains=query))
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_gender': gender,
        'current_master_category': master_category,
        'current_sub_category': sub_category,
        'current_article_type': article_type,
    }

    return render(request, 'products/products.html', context)


def product_page(request, product_id):
    """
    A view to show individual product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_page.html', context)
