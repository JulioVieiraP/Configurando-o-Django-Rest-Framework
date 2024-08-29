from django.urls import path, include
from rest_framework import routers

from api.viewsets import ProductViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
