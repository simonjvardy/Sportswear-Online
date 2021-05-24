# Code adapted from the CI Boutique Ado mini project

from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import (
    Product, Gender, MasterCategory, SubCategory, ArticleType, SpecialOffer)
from .forms import ProductForm


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all()
    sort = None
    direction = None
    query = None
    gender = None
    master_category = None
    sub_category = None
    article_type = None
    special_offer = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'gender' in request.GET:
            gender = request.GET['gender'].split(',')
            products = products.filter(
                gender__name__in=gender)
            gender = Gender.objects.filter(
                name__in=gender)

        if 'master_category' in request.GET:
            master_category = request.GET['master_category'].split(',')
            products = products.filter(
                master_category__name__in=master_category)
            master_category = MasterCategory.objects.filter(
                name__in=master_category)

        if 'sub_category' in request.GET:
            sub_category = request.GET['sub_category'].split(',')
            products = products.filter(
                sub_category__name__in=sub_category)
            sub_category = SubCategory.objects.filter(
                name__in=sub_category)

        if 'article_type' in request.GET:
            article_type = request.GET['article_type'].split(',')
            products = products.filter(
                article_type__name__in=article_type)
            article_type = ArticleType.objects.filter(
                name__in=article_type)

        if 'special_offer' in request.GET:
            special_offer = request.GET['special_offer'].split(',')
            products = products.filter(
                special_offer__name__in=special_offer)
            special_offer = SpecialOffer.objects.filter(
                name__in=special_offer)

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
                Q(article_type__name__icontains=query) |
                Q(special_offer__name__icontains=query))
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'search_term': query,
        'current_gender': gender,
        'current_master_category': master_category,
        'current_sub_category': sub_category,
        'current_article_type': article_type,
        'current_special_offer': special_offer,
        'current_sorting': current_sorting,
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


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # form post handler
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_page', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    # form post handler
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_page', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
