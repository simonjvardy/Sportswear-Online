from django.test import TestCase
from django.contrib.auth import get_user_model


class TestCheckoutViews(TestCase):
    """
    Tests the checkout page redirects correctly
    """

    def test_profile_page(self):
        response = self.client.get('/checkout', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response, '/products/', status_code=301, target_status_code=200)