from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for the user class"""

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
