from rest_framework import viewsets, permissions

from . import serializers
from . import models
from . import authentication


class taskViewSet(viewsets.ModelViewSet):
    """ViewSet for the task class"""

    queryset = models.task.objects.all()
    serializer_class = serializers.taskSerializer
    #permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.ExampleAuthentication]
    permission_classes = [authentication.CustomPermission]
