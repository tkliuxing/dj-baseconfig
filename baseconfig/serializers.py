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


class BaseConfigItemSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseConfigItem
        fields = (
            'pk',
            'name',
            'item_type'
        )


class BaseConfigItemSerializer(serializers.ModelSerializer):
    # category = BaseConfigCategorySerializer(read_only=True)
    item_id = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = models.BaseConfigItem
        fields = (
            'pk',
            'item_id',
            'category_name',
            'category_id',
            'name',
            'item_type',
            'str_max_length',
            'max_digits',
            'decimal_places',
            'allow_null',
            'unit',
        )

    def get_item_id(self, obj):
        return obj.pk

    def get_category_name(self, obj):
        return obj.category.name


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


