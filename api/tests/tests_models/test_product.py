import pytest

from api.models import Product

@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(name="Teste123", price=19.99, description="Testando a descrição do produto")
    assert product.name == "Teste123"
    assert product.description == "Testando a descrição do produto"
    assert product.price == 19.99