# Code adapted from CI Boutique Ado mini project

from django.contrib import admin
from .models import Order, OrderLineItem


class OderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = (
        'lineitem_total',
    )


class OrderAdmin(admin.ModelAdmin):
    inlines = (OderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'order_date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_cart',
        'stripe_pid'
    )

    fieldsets = (
        ('Order Details', {
            'fields': (
                'order_number',
                'order_date',
                'original_cart',
                'stripe_pid',
                'user_profile'
            )
        }),
        ('Customer', {
            'fields': (
                'first_name',
                'last_name'
            )
        }),
        ('Customer Details', {
            'fields': (
                'email',
                'telephone'
            )
        }),
        ('Customer Address', {
            'fields': (
                'address_line1',
                'address_line2',
                'town_or_city',
                'county',
                'postcode',
                'country'
            )
        }),
        ('Order Totals', {
            'fields': (
                'delivery_cost',
                'order_total',
                'grand_total'
            )
        }),

    )

    list_display = (
        'order_number',
        'order_date',
        'first_name',
        'last_name',
        'order_total',
        'delivery_cost',
        'grand_total',
    )

    ordering = (
        '-order_date',
    )


admin.site.register(Order, OrderAdmin)
