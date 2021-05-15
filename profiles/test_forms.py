from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):

    def test_form_fields_are_not_required(self):
        form = UserProfileForm({
            'default_telephone': '0123456789',
        })
        self.assertTrue(form.is_valid())
