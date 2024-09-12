from rest_framework.viewsets import ModelViewSet

from api.models import User
from api.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer