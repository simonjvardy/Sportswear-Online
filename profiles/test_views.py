from django.test import TestCase
from django.contrib.auth import get_user_model


class TestProfilesViews(TestCase):
    """
    Tests the profiles page renders the correct page
    Tests the product_page redirects correctly
    """
    # https://stackoverflow.com/questions/27841101/can-not-log-in-with-unit-test-in-django-allauth
    def setUp(self):
        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        user = User.objects.create_user(username, password=password)
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

    def test_profile_page(self):
        response = self.client.get('/profile', follow=True)
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'profiles/profile.html')
