import factory

from api.models import Product, User


class UserFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("pystr")
    username = factory.Faker("pystr")
    phone_number = factory.Faker("pyint")
    email = factory.Faker("pystr")
    password = factory.Faker("pystr")
    city = factory.Faker("pystr")
    address = factory.Faker("pystr")

    class Meta:
        model = User


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("pystr")
    description = factory.Faker("pystr")
    price = factory.Faker("random_int", min=1, max=100)

    class Meta:
        model = Product
