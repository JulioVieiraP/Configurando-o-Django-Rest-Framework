import pytest

from api.models import User
from api.serializers import UserSerializer

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create(
        name = 'testuser',
        username="testeuser123",
        phone_number = '123456789',
        email="testeuser123@example.com", 
        password="teste123",
        city = 'Test City',
        address = 'Test Address'
    )
    serializer = UserSerializer(instance=user)
    data = serializer.data

    assert data['name'] == 'testuser'
    assert data['username'] == 'testeuser123'
    assert data['phone_number'] == '123456789'
    assert data['email'] == 'testeuser123@example.com'
    assert data['password'] == 'teste123'
    assert data['city'] == 'Test City'
    assert data['address'] == 'Test Address'