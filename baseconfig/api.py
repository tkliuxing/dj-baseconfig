from . import models
from . import serializers
from rest_framework import viewsets, permissions


class BaseConfigCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the BaseConfigCategory class"""

    queryset = models.BaseConfigCategory.objects.all()
    serializer_class = serializers.BaseConfigCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BaseConfigItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the BaseConfigItem class"""

    queryset = models.BaseConfigItem.objects.all()
    serializer_class = serializers.BaseConfigItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BaseConfigValueViewSet(viewsets.ModelViewSet):
    """ViewSet for the BaseConfigValue class"""

    queryset = models.BaseConfigValue.objects.all()
    serializer_class = serializers.BaseConfigValueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

