import json
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status

from api.factories import OrderFactory, ProductFactory, UserFactory


@pytest.fixture
def auth_client(db):
    user = UserFactory()
    token, _ = Token.objects.get_or_create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    return client


@pytest.mark.django_db
def test_order(auth_client):
    product = ProductFactory(name="mouse", price=100.00, description="Descrição")
    order = OrderFactory(product=[product])

    url = reverse("order-list")
    response = auth_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    order_data = json.loads(response.content)

    assert order_data["results"][0]["product"][0]["name"] == product.name
    assert order_data["results"][0]["product"][0]["price"] == product.price
    assert order_data["results"][0]["product"][0]["description"] == product.description
