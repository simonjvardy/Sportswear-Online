from django.test import TestCase

# Create your tests here.


class TestProductsViews(TestCase):
    """
    Tests the products page renders the correct page
    """
    def test_all_products_page(self):
        response = self.client.get('/products/', follow=True)
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'products/products.html')

    def test_product_page(self):
        response = self.client.get('/products', follow=True)
        self.assertRedirects(response, '/products/', status_code=301, target_status_code=200)
