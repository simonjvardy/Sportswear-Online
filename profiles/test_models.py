from django.test import TestCase
from .models import UserProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your tests here.


class TestProfilesModels(TestCase):
    """
    Tests the products page renders the correct page
    Tests the product_page redirects correctly
    """
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_user_profile_string_method_returns_name(self):
        test_user = UserProfile.objects.create(user=self.user)
        instance.userprofile.save()
        self.assertTrue(test_user)
