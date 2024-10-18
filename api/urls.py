from django.urls import path, include
from rest_framework import routers

from api.viewsets import ProductViewSet, OrderViewSet

router = routers.SimpleRouter()
router.register(r"product", ProductViewSet, basename="product")
router.register(r"order", OrderViewSet, basename="order")

urlpatterns = [path("", include(router.urls))]
