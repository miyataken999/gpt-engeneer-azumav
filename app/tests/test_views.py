from django.test import TestCase
from rest_framework.test import APIClient
from .models import Shop

class ShopViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Shop.objects.create(name='Test Shop', category='Fluorescence', subcategory='CUT PROPORTION', price=2.50)

    def test_shop_view(self):
        response = self.client.get('/shops/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)