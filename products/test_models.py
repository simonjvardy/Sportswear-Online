from django.test import TestCase
from .models import (
    Product, Gender, ArticleType, MasterCategory, SubCategory)


class TestProductsModels(TestCase):
    """
    Test the string methods return the correct model name fields
    """

    def test_products_string_method_returns_name(self):
        product = Product.objects.create(
            price=5.99,
            discount_price=4.99,
            sku='abc123',
            name='Test Product',
            product_description='Test Product Description',
        )
        self.assertEqual(str(product), 'Test Product')

    def test_gender_string_method_returns_display_name(self):
        gender = Gender.objects.create(
            name='Test Gender',
            display_name='Test Display Name',
        )
        self.assertEqual(str(gender), 'Test Gender')

    def test_article_type_string_method_returns_display_name(self):
        article_type = ArticleType.objects.create(
            name='Test Article Type',
            display_name='Test Display Name',
        )
        self.assertEqual(str(article_type), 'Test Article Type')

    def test_master_category_string_method_returns_display_name(self):
        master_category = MasterCategory.objects.create(
            name='Test Master Category',
            display_name='Test Display Name',
        )
        self.assertEqual(str(master_category), 'Test Master Category')

    def test_sub_category_method_returns_display_name(self):
        sub_category = SubCategory.objects.create(
            name='Test Sub Category',
            display_name='Test Display Name',
        )
        self.assertEqual(str(sub_category), 'Test Sub Category')
