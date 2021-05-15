from django.test import TestCase


# Create your tests here.


class TestProfilesViews(TestCase):
    """
    Tests the products page renders the correct page
    Tests the product_page redirects correctly
    """

    def test_profile_page(self):
        response = self.client.get('/profile', follow=True)
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'profiles/profile.html')
