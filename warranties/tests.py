from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product, Warranty



class ProductViewSetTest(APITestCase):
    def test_create_product(self):
        url = reverse('product-list')
        data = {
            "name": "Washing Machine",
            "price": 499.99,
            "product_code": "WM12345"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, "Washing Machine")

    def test_get_products(self):
        Product.objects.create(name="Microwave", price=299.99, product_code="MW56789")
        url = reverse('product-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)



class WarrantyViewSetTest(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Fridge", price=799.99, product_code="FRD98765")

    def test_create_warranty(self):
        url = reverse('warranty-list')
        data = {
            "product": self.product.id,
            "warranty_code": "WR123456",
            "customer_name": "Ali Rezaei"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Warranty.objects.count(), 1)
        self.assertEqual(Warranty.objects.get().customer_name, "Ali Rezaei")

    def test_get_warranties(self):
        Warranty.objects.create(product=self.product, warranty_code="WR987654", customer_name="Sara Jafari")
        url = reverse('warranty-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
