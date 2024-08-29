import factory

from django.contrib.auth.models import User
from api.models import Product

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    class Meta:
        model = User
    


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('product_name')
    description = factory.Faker('text')
    price = factory.Faker('random_number', min=1, max=100)
    
    class Meta:
        model = Product
