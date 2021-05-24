from django.test import TestCase


class TestProductsViews(TestCase):
    """
    Tests the products page renders the correct page
    Tests the product_page redirects correctly
    """

    def test_all_products_page(self):
        response = self.client.get('/products', follow=True)
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'products/products.html')

    def test_product_page(self):
        response = self.client.get('/products')
        self.assertRedirects(
            response, '/products/', status_code=301, target_status_code=200)
