from rest_framework import serializers

from . import models


class BaseConfigCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseConfigCategory
        fields = (
            'pk',
            'name',
            'is_choice_source',
            'create_time',
        )


class BaseConfigItemSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseConfigItem
        fields = (
            'pk',
            'name',
            'sort_number',
            'item_type',
            'item_type_display',
            'default_value',
            'remark',
        )


class BaseConfigItemSerializer(serializers.ModelSerializer):
    item_id = serializers.CharField(source='pk', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = models.BaseConfigItem
        fields = (
            'pk',
            'sort_number',
            'item_id',
            'category_name',
            'category_id',
            'category',
            'name',
            'item_type',
            'item_type_display',
            'is_choices',
            'is_multiple_choices',
            'str_max_length',
            'int_max', 'int_min', 'int_max_eq', 'int_min_eq',
            'max_digits',
            'decimal_places',
            'decimal_max', 'decimal_min', 'decimal_max_eq', 'decimal_min_eq',
            'float_max', 'float_min', 'float_max_eq', 'float_min_eq',
            'allow_null',
            'unit',
            'str_default',
            'bool_default',
            'int_default',
            'float_default',
            'decimal_default',
            'date_default',
            'datetime_default',
            'time_default',
            'choices_source',
            'choices_source_values',
            'default_value',
            'remark',
        )


class BaseConfigValueSerializer(serializers.ModelSerializer):
    item_info = BaseConfigItemSerializer(read_only=True, required=False)
    value = serializers.CharField(
        label='值', help_text='值'
    )

    class Meta:
        model = models.BaseConfigValue
        fields = (
            'pk',
            'value',
            'value_display',
            'item',
            'item_display',
            'item_info',
            'str_value',
            'bool_value',
            'int_value',
            'float_value',
            'decimal_value',
            'date_value',
            'datetime_value',
            'time_value',
            'create_time',
            'sort_number',
        )

    def create(self, validated_data):
        instance = super().create(validated_data)
        if 'value' in validated_data:
            instance.value = validated_data['value']
            instance.save()
        return instance

    def update(self, instance, validated_data):
        new_instance = super().update(instance, validated_data)
        if 'value' in validated_data:
            new_instance.value = validated_data['value']
            new_instance.save()
        return new_instance


class BaseConfigFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseConfigFileUpload
        fields = (
            'file',
            'create_time'
        )
