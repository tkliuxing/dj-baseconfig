from . import models

from rest_framework import serializers


class BaseConfigCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BaseConfigCategory
        fields = (
            'pk',
            'name',
            'create_time',
        )


class BaseConfigItemSerializer(serializers.ModelSerializer):
    category = BaseConfigCategorySerializer(read_only=True)

    class Meta:
        model = models.BaseConfigItem
        fields = (
            'pk',
            'category',
            'category_id',
            'name',
            'item_type',
            'str_max_length',
            'max_digits',
            'decimal_places',
            'allow_null',
            'unit',
        )


class BaseConfigValueSerializer(serializers.ModelSerializer):
    item = BaseConfigItemSerializer(read_only=True)

    class Meta:
        model = models.BaseConfigValue
        fields = (
            'pk',
            'item',
            'item_id',
            'str_value',
            'bool_value',
            'int_value',
            'float_value',
            'decimal_value',
            'create_time',
        )


