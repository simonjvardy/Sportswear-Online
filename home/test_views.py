from django.test import TestCase

# Create your tests here.


class TestHomeViews(TestCase):
    """
    Tests the home page renders the correct page
    """
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'home/index.html')
