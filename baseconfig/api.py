from . import models
from . import serializers
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend


class BaseConfigCategoryViewSet(viewsets.ModelViewSet):
    """基础类别API"""

    queryset = models.BaseConfigCategory.objects.all()
    serializer_class = serializers.BaseConfigCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'is_choice_source',)


class BaseConfigCategoryNamedViewSet(viewsets.ModelViewSet):
    """根据name而不是PK获取基础类别详情"""

    queryset = models.BaseConfigCategory.objects.all()
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
    serializer_class = serializers.BaseConfigCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'is_choice_source',)


class BaseConfigItemViewSet(viewsets.ModelViewSet):
    """基础配置项定义API"""

    queryset = models.BaseConfigItem.objects.order_by('category', 'sort_number', 'pk')
    serializer_class = serializers.BaseConfigItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category__name', 'name', 'allow_null', 'category',)


class BaseConfigValueViewSet(viewsets.ModelViewSet):
    """基础配置项值API"""

    queryset = models.BaseConfigValue.objects.all()
    serializer_class = serializers.BaseConfigValueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BaseConfigFileUploadViewSet(viewsets.ModelViewSet):
    """基础配置项文件API"""

    queryset = models.BaseConfigFileUpload.objects.all()
    serializer_class = serializers.BaseConfigFileUploadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
