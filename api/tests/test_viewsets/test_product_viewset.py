import json
import pytest

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from api.factories import ProductFactory
from api.models import Product

@pytest.mark.django_db
class TestProductViewSet(APITestCase):
    client = APIClient()
    
    def setUp(self):
        self.url = "product-list"
        
        self.product = ProductFactory(
            name='Mouse',
            description='Mouse description',
            price=100
        )
    
    def test_get_all_products(self):
        response = self.client.get(reverse(self.url))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)
        
        self.assertEqual(product_data[0]['name'], self.product.name)
        self.assertEqual(product_data[0]['description'], self.product.description)
    
    def test_create_product(self):
        data = json.dumps({
            'name': 'Teclado',
            'description': 'Teclado descritivo',
            'price': 200
        })
        
        response = self.client.post(reverse(self.url), data=data, content_type='application/json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        created_product = Product.objects.get(name='Teclado')
        
        self.assertEqual(created_product.name, 'Teclado')
        self.assertEqual(created_product.price, 200)
        
    