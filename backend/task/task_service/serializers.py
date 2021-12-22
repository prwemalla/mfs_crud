from rest_framework import serializers

from . import models


class taskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.task
        fields = [
            "id",
            "created",
            "description",
            "name",
            "last_updated",
            "user",
            "status",
        ]
