import pytest

from api.models import User

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create(name="Teste User", username="testeuser", phone_number="1234567890", email="testeuser@gmail.com", password="testeuser123", city="Cidade Teste", address="Rua Teste, 123")
    assert user.name == "Teste User"
    assert user.username == "testeuser"
    assert user.phone_number == "1234567890"
    assert user.email == "testeuser@gmail.com"
    assert user.password == "testeuser123"
    assert user.city == "Cidade Teste"
    assert user.address == "Rua Teste, 123"