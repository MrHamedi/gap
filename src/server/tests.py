from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Server, Channel, Category


def user_creator(email="test@mail.com", password="test_password"):
    return get_user_model().objects.create_user(email=email, password=password)


class ServerModelTests(TestCase):

    def setUp(self):
        self.owner = user_creator()
        self.category = Category.objects.create(name="نوع ۱", description="نوع اول")
        self.server = Server.objects.create(name="سرور ۱", 
                                            owner=self.owner,
                                            description="سرور ۱",
                                            category=self.category
                                            )

    def test_Server_created(self):
        self.assertEqual(Server.objects.count(), 1)

