import pytest

from api.models import Product
from api.serializers import ProductSerializer


@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        name="teste123", description="Testando a descrição do produto", price=19.99
    )

    serializer = ProductSerializer(instance=product)
    data = serializer.data

    assert data["name"] == "teste123"
    assert data["description"] == "Testando a descrição do produto"
    assert data["price"] == 19.99
