from django.contrib import admin
from .models import (
    Product, Gender, ArticleType, MasterCategory, SubCategory, SpecialOffer
)


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'sku',
                ('name', 'product_description'),
                ('price', 'discount_price'),
                'image')
        }),
        ('Category Selections', {
            'classes': ('collapse',),
            'fields': (
                'gender',
                'master_category',
                'sub_category',
                'article_type',
                'special_offer'),
        }),
    )

    list_display = (
        'sku',
        'name',
        'product_description',
        'price',
        'discount_price',
        'image'
    )


class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class GenderAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class MasterCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(MasterCategory, MasterCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(SpecialOffer, SpecialOfferAdmin)
