import pytest
import json
from django.urls import reverse
from rest_framework import status
from api.models import User
from api.serializers import UserSerializer

@pytest.mark.django_db
def test_create_user(client):
    url = reverse('user-list')

    
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'name': 'Test User',
        'password': 'testpassword', 
        'phone_number': '123456789',
        'city': 'Test City',
        'address': 'Test Address'
    }

    response = client.post(url, data=json.dumps(data), content_type='application/json')

    assert response.status_code == status.HTTP_201_CREATED
    user = json.loads(response.content)
    
    assert user['username'] == data.get('username')
    assert user['email'] == data.get('email')
    assert user['name'] == data.get('name')
    assert user['password'] == data.get('password')
    assert user['phone_number'] == data.get('phone_number')
    assert user['city'] == data.get('city')
    assert user['address'] == data.get('address')
    
