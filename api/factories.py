import factory

from api.models import Product, User

class UserFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    username = factory.Faker('user_name')
    phone_number = factory.Faker('phone_number')
    email = factory.Faker('email')
    password = factory.Faker('password')
    city = factory.Faker('city')
    address = factory.Faker('address')
    class Meta:
        model = User
    


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('product_name')
    description = factory.Faker('text')
    price = factory.Faker('random_number', min=1, max=100)
    
    class Meta:
        model = Product
