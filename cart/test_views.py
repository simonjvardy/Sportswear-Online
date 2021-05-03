from django.test import TestCase

# Create your tests here.


class TestCartViews(TestCase):
    """
    Tests the home page renders the correct page
    """
    def test_all_products_page(self):
        response = self.client.get('/cart', follow=True)
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'cart/cart.html')
