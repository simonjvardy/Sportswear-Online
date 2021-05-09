from django.test import TestCase
from .models import (
    Order, OrderLineItem)
from products.models import Product


class TestCheckoutModels(TestCase):
    """
    Test the string methods return the correct model name fields
    """

    def setUp(self):
        self.product = Product.objects.create(
            price=5.99,
            discount_price=4.99,
            sku='abc123',
            name='Test Product',
            product_description='Test Product Description',
        )
        self.order = Order.objects.create(
            order_number='Test Order',
            order_date='2021-05-09 14:30:59',
            first_name='John',
            last_name='Smith',
            email='test@email.com',
            telephone='123456789',
            address_line1='Address Line 1',
            address_line2='Address Line 2',
            town_or_city='City',
            county='County',
            postcode='AB99-XYZ',
            country='GB',
            delivery_cost=2.50,
            order_total=10.99,
            grand_total=13.49,
        )

    def test_order_string_method_returns_order_number(self):
        order = Order.objects.get(
            order_number='Test Order'
        )
        self.assertEqual(str(order), 'Test Order')
