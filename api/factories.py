import factory

from django.contrib.auth.models import User
from api.models import Product
from api.models.order import Order


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("pystr")
    username = factory.Faker("pystr")

    class Meta:
        model = User


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("pystr")
    description = factory.Faker("pystr")
    price = factory.Faker("random_int", min=1, max=100)

    class Meta:
        model = Product


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.product.add(product)

    class Meta:
        model = Order
        skip_postgeneration_save = True
