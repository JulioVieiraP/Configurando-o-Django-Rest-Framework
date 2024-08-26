import factory

from django.contrib.auth.models import User
from api.models import Product

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
    
    username = factory.Faker('user_name')
    email = factory.Faker('email')


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('product_name')
    description = factory.Faker('text')
    price = factory.Faker('random_number', min=1, max=100)