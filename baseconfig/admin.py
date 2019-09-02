from django.contrib import admin
from django import forms
from .models import BaseConfigCategory, BaseConfigItem, BaseConfigValue


class BaseConfigCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time']
    readonly_fields = ['name', 'create_time']

admin.site.register(BaseConfigCategory, BaseConfigCategoryAdmin)


class BaseConfigItemAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'item_type']
    readonly_fields = ['category', 'name', 'item_type']

admin.site.register(BaseConfigItem, BaseConfigItemAdmin)


class BaseConfigValueAdmin(admin.ModelAdmin):
    list_display = ['item', 'str_value', 'bool_value', 'int_value', 'float_value', 'decimal_value', 'create_time']
    readonly_fields = ['item', 'str_value', 'bool_value', 'int_value', 'float_value', 'decimal_value', 'create_time']

admin.site.register(BaseConfigValue, BaseConfigValueAdmin)


