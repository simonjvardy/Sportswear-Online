from django.test import TestCase
from .forms import OrderForm


class TestorderForm(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'first_name',
            'last_name',
            'email',
            'telephone',
            'address_line1',
            'address_line2',
            'town_or_city',
            'county',
            'postcode',
            'country'
        ))

    def test_firstname_is_required(self):
        form = OrderForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.')

    def test_lastname_is_required(self):
        form = OrderForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(
            form.errors['last_name'][0], 'This field is required.')

    def test_email_is_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_telephone_is_required(self):
        form = OrderForm({'telephone': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('telephone', form.errors.keys())
        self.assertEqual(
            form.errors['telephone'][0], 'This field is required.')

    def test_addressline1_is_required(self):
        form = OrderForm({'address_line1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('address_line1', form.errors.keys())
        self.assertEqual(
            form.errors['address_line1'][0], 'This field is required.')

    def test_town_or_city_is_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_country_is_required(self):
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_remaining_fields_are_not_required(self):
        form = OrderForm({
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@email.com',
            'telephone': '123456789',
            'address_line1': 'Test Address',
            'town_or_city': 'Test Town',
            'country': 'GB'
        })
        self.assertTrue(form.is_valid())