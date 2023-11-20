from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class UserTestCase(TestCase):

    def setUp(self):
        username = "username"
        email = "user@gmail.com"
        password = "pass"
        self.user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password,
        )

    def test_user_credentials(self):
        self.assertEqual(self.user.username, "username")
        self.assertEqual(self.user.email, "user@gmail.com")
        self.assertTrue(self.user.check_password("pass"))

    def test_email_normalized(self):
        user = get_user_model().objects.create_user(username="new _username",
                                                    email="example@GMAIL.COM", 
                                                    password='pass'
        )
        user.save()
        self.assertEqual(user.email, 'example@gmail.com')

    def test_credentials_superuser(self):
        username="super_user_username"
        email = "superuser@gmail.com"
        password = "pass"
        user = get_user_model().objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
