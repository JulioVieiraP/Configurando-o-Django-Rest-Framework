import json
import pytest
from django.urls import reverse
from rest_framework import status

from api.factories import ProductFactory
from api.models import Product

@pytest.mark.django_db
def test_get_all_products(client):
    url = reverse('product-list')
    
    product = ProductFactory(
        name='Mouse',
        description='Mouse description',
        price=100
    )
    
    response = client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    product_data = response.json()
    
    assert product_data[0]['name'] == product.name
    assert product_data[0]['description'] == product.description

@pytest.mark.django_db
def test_create_product(client):
    url = reverse('product-list')
    
    data = {
        'name': 'Teclado',
        'description': 'Teclado descritivo',
        'price': 200
    }
    
    response = client.post(url, data=json.dumps(data), content_type='application/json')
    
    assert response.status_code == status.HTTP_201_CREATED
    
    created_product = Product.objects.get(name='Teclado')
    
    assert created_product.name == 'Teclado'
    assert created_product.price == 200
