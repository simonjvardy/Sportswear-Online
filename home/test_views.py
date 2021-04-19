from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):
    """
    Test home page renders correct page
    """
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'home/index.html')
