from django import test
from django.contrib.auth import get_user_model

from .forms import UserCreationForm
from .models import CustomeUser


class UserTest(test.TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username="test_username",
            first_name="first",
            last_name="last",
            password="test_password")
        self.user.set_password("test_password")
        self.user.save()

    def test_user(self):
        self.assertIsInstance(self.user, CustomeUser)
        self.assertEqual(self.user.username, "test_username")
        self.assertEqual(self.user.first_name, "first")
        self.assertEqual(self.user.last_name, "last")

    def test_user_creation_form(self):
        data_entry = {
            "first_name": "first",
            "last_name": "last",
            "password": "password",
            "password2": "password",
            "username": "username",
        }
        form = UserCreationForm(data_entry)
        self.assertTrue(form.is_valid())

    def test_error_user_creation_form(self):
        data_entry = {
            "first_name": "first",
            "last_name": "last",
            "password": "password",
            "password2": "un_matching_password2",
            "username": "username",
        }
        form = UserCreationForm(data_entry)
        self.assertFalse(form.is_valid())
