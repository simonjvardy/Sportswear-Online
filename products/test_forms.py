from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    """
    Tests to verify form fields are required
    """

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProductForm()
        self.assertEqual(form.Meta.fields, (
            '__all__'
        ))

    def test_image_is_required(self):
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(
            form.errors['price'][0], 'This field is required.')

    def test_lastname_is_required(self):
        form = ProductForm({'discount_price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('discount_price', form.errors.keys())
        self.assertEqual(
            form.errors['discount_price'][0], 'This field is required.')

    def test_email_is_required(self):
        form = ProductForm({'sku': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('sku', form.errors.keys())
        self.assertEqual(
            form.errors['sku'][0], 'This field is required.')

    def test_telephone_is_required(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')

    def test_addressline1_is_required(self):
        form = ProductForm({'product_description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('product_description', form.errors.keys())
        self.assertEqual(
            form.errors['product_description'][0], 'This field is required.')
