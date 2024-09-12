from rest_framework.viewsets import ModelViewSet

from api.models import Product
from api.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer
