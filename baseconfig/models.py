from decimal import Decimal
from django.db import models
from django.contrib.contenttypes.models import ContentType


class BaseConfigCategory(models.Model):
    """基础类别"""
    name = models.CharField('类别名称', max_length=255)
    content_types = models.ManyToManyField(ContentType, verbose_name='模型类型',
                                           help_text="使用模型反查时需要填写", blank=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    
    class Meta:
        verbose_name = '基础类别'
        verbose_name_plural = verbose_name
        ordering = ['create_time']

    def __str__(self):
        return self.name


class BaseConfigItem(models.Model):
    """基础配置项定义"""
    ITEM_TYPES = (
        ('str', '字符串'),
        ('bool', '布尔值'),
        ('int', '整数'),
        ('float', '浮点数'),
        ('decimal', '精确浮点数'),
    )
    category = models.ForeignKey('BaseConfigCategory', on_delete=models.CASCADE, verbose_name='基础类别')
    name = models.CharField('配置项名称', max_length=255)
    item_type = models.CharField('配置项类型', max_length=20, choices=ITEM_TYPES, default='str')
    str_max_length = models.PositiveSmallIntegerField('字符串值长度', default=127, null=True, blank=True)
    max_digits = models.PositiveSmallIntegerField('精确浮点数总位数', default=5, null=True, blank=True)
    decimal_places = models.PositiveSmallIntegerField('精确浮点数小数位数', default=2, null=True, blank=True)
    allow_null = models.BooleanField('允许为空', default=True)
    unit = models.CharField('数值单位', max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = '基础配置项定义'
        verbose_name_plural = verbose_name
        ordering = ['category', 'pk']

    def __str__(self):
        return self.name


class BaseConfigValue(models.Model):
    """基础配置项值"""
    item = models.ForeignKey('BaseConfigItem', on_delete=models.CASCADE, verbose_name='基础类别')
    str_value = models.TextField('字符串值', null=True, blank=True)
    bool_value = models.BooleanField('布尔值', null=True, blank=True)
    int_value = models.IntegerField('整数值', null=True, blank=True)
    float_value = models.FloatField('浮点数值', null=True, blank=True)
    decimal_value = models.DecimalField('精确浮点数值', null=True, blank=True, max_digits=30, decimal_places=5)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    
    class Meta:
        verbose_name = '基础配置项值'
        verbose_name_plural = verbose_name
        ordering = ['item']

    def __str__(self):
        return "{0}: {1} {2}".format(self.item.name, str(self.value), self.item.unit or '')

    def get_value(self):
        if self.item.item_type == 'str':
            return self.str_value
        elif self.item.item_type == 'bool':
            return self.bool_value
        elif self.item.item_type == 'int':
            return self.int_value
        elif self.item.item_type == 'float':
            return self.float_value
        elif self.item.item_type == 'decimal':
            return self.decimal_value
        raise TypeError('BaseConfigItem {0} does not set item_type'.format(self.item.pk))
    
    def set_value(self, value):
        if not self.item or not self.item.item_type:
            raise TypeError('BaseConfigItem {0} does not set item_type'.format(self.item.pk))
        if self.item.item_type == 'str':
            self.str_value = str(value)
        elif self.item.item_type == 'bool':
            self.bool_value = bool(value)
        elif self.item.item_type == 'int':
            self.int_value = int(value)
        elif self.item.item_type == 'float':
            self.float_value = float(value)
        elif self.item.item_type == 'decimal':
            self.decimal_value = Decimal(value)
        else:
            raise TypeError('BaseConfigItem {0} item_type error'.format(self.item.pk))
    
    value = property(get_value, set_value)

    class Meta:
        verbose_name = '基础配置项值'
        verbose_name_plural = verbose_name
        ordering = ['item', '-create_time']
