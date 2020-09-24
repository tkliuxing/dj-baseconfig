from django.contrib import admin
from .models import BaseConfigCategory, BaseConfigItem, BaseConfigValue


class BaseConfigItemInline(admin.StackedInline):
    model = BaseConfigItem
    fk_name = 'category'
    fields = (
        'sort_number', 'category', 'name', 'item_type', 'is_choices', 'is_multiple_choices', 'str_max_length',
        'int_max', 'int_min', 'int_max_eq', 'int_min_eq',
        'max_digits', 'decimal_places', 'decimal_max', 'decimal_min', 'decimal_max_eq', 'decimal_min_eq',
        'float_max', 'float_min', 'float_max_eq', 'float_min_eq',
        'allow_null', 'unit',
        'str_default', 'bool_default', 'int_default', 'float_default', 'decimal_default',
        'date_default', 'datetime_default', 'time_default',
    )


class BaseConfigCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time']
    inlines = [BaseConfigItemInline]


admin.site.register(BaseConfigCategory, BaseConfigCategoryAdmin)


class BaseConfigItemAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'item_type']


admin.site.register(BaseConfigItem, BaseConfigItemAdmin)


class BaseConfigValueInline(admin.TabularInline):
    model = BaseConfigValue
    fields = ['str_value', 'bool_value', 'int_value', 'float_value', 'decimal_value', 'create_time']


class BaseConfigValueAdmin(admin.ModelAdmin):
    list_display = ['item', 'str_value', 'bool_value', 'int_value', 'float_value', 'decimal_value', 'create_time']
    raw_id_fields = ['item']


admin.site.register(BaseConfigValue, BaseConfigValueAdmin)
