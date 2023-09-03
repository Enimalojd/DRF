from rest_framework.test import APITestCase
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()


class ServicesApiTestCase(APITestCase):
    def test_get(self):
        from django.urls import reverse
        url = reverse('services-list')
        print(url)
        response = self.client.get(url)
        print(response)
