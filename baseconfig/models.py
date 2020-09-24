from decimal import Decimal

from django.contrib.contenttypes.models import ContentType
from django.db import models


class BaseConfigCategory(models.Model):
    """基础类别"""
    name = models.CharField('类别名称', max_length=255)
    is_choice_source = models.BooleanField(
        '选项类型字段数据源', default=False, help_text='选项类型字段数据源'
    )
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
        ('date', '日期'),
        ('year', '年份'),
        ('datetime', '日期时间'),
        ('time', '时间'),
        ('file', '文件'),
    )
    sort_number = models.PositiveIntegerField('排序编号', default=1, help_text='排序编号')
    category = models.ForeignKey('BaseConfigCategory', on_delete=models.CASCADE, verbose_name='基础类别')
    name = models.CharField('配置项名称', max_length=255)
    item_type = models.CharField('配置项类型', max_length=20, choices=ITEM_TYPES, default='str')
    is_choices = models.BooleanField('是否为选项类型', default=False, help_text='是否为选项类型')
    is_multiple_choices = models.BooleanField('是否为多选类型', default=False, help_text='是否为多选类型')

    str_max_length = models.PositiveSmallIntegerField('字符串值长度', default=127, null=True, blank=True)

    int_max = models.IntegerField('整数最大值', null=True, blank=True, help_text='整数最大值')
    int_min = models.IntegerField('整数最小值', null=True, blank=True, help_text='整数最小值')
    int_max_eq = models.BooleanField('整数最大值包含等于', default=False, help_text='整数最大值包含等于')
    int_min_eq = models.BooleanField('整数最小值包含等于', default=False, help_text='整数最小值包含等于')

    max_digits = models.PositiveSmallIntegerField('精确浮点数总位数', default=5, null=True, blank=True)
    decimal_places = models.PositiveSmallIntegerField('精确浮点数小数位数', default=2, null=True, blank=True)
    decimal_max = models.DecimalField('精确浮点数最大值', null=True, blank=True, help_text='精确浮点数最大值', max_digits=30,
                                      decimal_places=5)
    decimal_min = models.DecimalField('精确浮点数最小值', null=True, blank=True, help_text='精确浮点数最小值', max_digits=30,
                                      decimal_places=5)
    decimal_max_eq = models.BooleanField('精确浮点数最大值包含等于', default=False, help_text='精确浮点数最大值包含等于')
    decimal_min_eq = models.BooleanField('精确浮点数最小值包含等于', default=False, help_text='精确浮点数最小值包含等于')

    float_max = models.FloatField('浮点数最大值', null=True, blank=True, help_text='浮点数最大值')
    float_min = models.FloatField('浮点数最小值', null=True, blank=True, help_text='浮点数最小值')
    float_max_eq = models.BooleanField('浮点数最大值包含等于', default=False, help_text='浮点数最大值包含等于')
    float_min_eq = models.BooleanField('浮点数最小值包含等于', default=False, help_text='浮点数最小值包含等于')

    allow_null = models.BooleanField('允许为空', default=True)
    unit = models.CharField('数值单位', max_length=10, null=True, blank=True)
    str_default = models.TextField('字符串默认值', null=True, blank=True, help_text='字符串默认值')
    bool_default = models.BooleanField('布尔值默认值', null=True, blank=True, help_text='布尔值默认值')
    int_default = models.IntegerField('整数默认值', null=True, blank=True, help_text='整数默认值')
    float_default = models.FloatField('浮点数默认值', null=True, blank=True, help_text='浮点数默认值')
    decimal_default = models.DecimalField(
        '精确浮点数默认值', null=True, blank=True, help_text='精确浮点数默认值', decimal_places=5, max_digits=20
    )
    date_default = models.DateField('日期默认值', null=True, blank=True, help_text='日期默认值')
    datetime_default = models.DateTimeField('日期时间默认值', null=True, blank=True, help_text='日期时间默认值')
    time_default = models.TimeField('时间默认值', null=True, blank=True, help_text='时间默认值')
    choices_source = models.ForeignKey(
        'BaseConfigCategory', on_delete=models.SET_NULL, null=True, blank=True,
        help_text='选项字段数据源', verbose_name='选项字段数据源', related_name='+'
    )
    remark = models.TextField(
        '备注', null=True, blank=True, help_text='备注'
    )

    class Meta:
        verbose_name = '基础配置项定义'
        verbose_name_plural = verbose_name
        ordering = ['category', 'sort_number', 'pk']

    @property
    def default_value(self):
        if self.is_choices:
            return None
        if self.item_type == 'str':
            return self.str_default
        elif self.item_type == 'bool':
            return self.bool_default
        elif self.item_type in ['int', 'year']:
            return self.int_default
        elif self.item_type == 'float':
            return self.float_default
        elif self.item_type == 'decimal':
            return self.decimal_default
        elif self.item_type == 'date':
            return self.date_default
        elif self.item_type == 'datetime':
            return self.datetime_default
        elif self.item_type == 'time':
            return self.time_default
        elif self.item_type == 'file':
            return ''
        raise TypeError('BaseConfigItem {0} does not set item_type'.format(self.pk))

    @property
    def choices_source_values(self):
        if self.choices_source:
            sources = self.choices_source.baseconfigitem_set.all()
            return [i.default_value for i in sources]
        return []

    def __str__(self):
        return self.name

    @property
    def item_type_display(self):
        return dict(self.ITEM_TYPES)[self.item_type]


class BaseConfigValue(models.Model):
    """基础配置项值"""
    item = models.ForeignKey('BaseConfigItem', on_delete=models.CASCADE, verbose_name='基础类别')
    str_value = models.TextField('字符串值', null=True, blank=True)
    bool_value = models.BooleanField('布尔值', null=True, blank=True)
    int_value = models.IntegerField('整数值', null=True, blank=True)
    float_value = models.FloatField('浮点数值', null=True, blank=True)
    decimal_value = models.DecimalField('精确浮点数值', null=True, blank=True, max_digits=30, decimal_places=5)
    date_value = models.DateField('日期', null=True, blank=True)
    datetime_value = models.DateTimeField('日期时间', null=True, blank=True)
    time_value = models.TimeField('时间', null=True, blank=True)
    file_value = models.TextField('文件URL', null=True, blank=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    sort_number = models.PositiveIntegerField('排序编号', default=1, help_text='排序编号')
    choices_value = models.ForeignKey(
        'BaseConfigItem', on_delete=models.CASCADE, related_name='+',
        verbose_name='单选值', null=True, blank=True, help_text='单选值'
    )
    multi_choices_value = models.ManyToManyField(
        'BaseConfigItem', related_name='+',
        verbose_name='多选值', blank=True, help_text='多选值'
    )
    raw_value = models.TextField(
        '原始值', null=True, blank=True, help_text='原始值'
    )

    class Meta:
        verbose_name = '基础配置项值'
        verbose_name_plural = verbose_name
        ordering = ['item', 'sort_number', '-create_time']

    @property
    def item_display(self):
        return self.item.name

    def __str__(self):
        return "{0}: {1} {2}".format(self.item.name, str(self.value), self.item.unit or '')

    def get_value(self):
        if self.item.is_choices and self.item.is_multiple_choices:
            return list(self.multi_choices_value.all().values_list('pk', flat=True))
        if self.item.is_choices and not self.item.is_multiple_choices:
            return self.choices_value_id if self.choices_value else None
        if self.item.item_type == 'str':
            return self.str_value
        elif self.item.item_type == 'bool':
            return self.bool_value
        elif self.item.item_type in ['int', 'year']:
            return self.int_value
        elif self.item.item_type == 'float':
            return self.float_value
        elif self.item.item_type == 'decimal':
            return self.decimal_value
        elif self.item.item_type == 'date':
            return self.date_value
        elif self.item.item_type == 'datetime':
            return self.datetime_value
        elif self.item.item_type == 'time':
            return self.time_value
        elif self.item.item_type == 'file':
            return self.file_value
        raise TypeError('BaseConfigItem {0} does not set item_type'.format(self.item.pk))

    def set_value(self, value):
        self.raw_value = str(value)
        if self.item.is_choices and self.item.is_multiple_choices:
            if not isinstance(value, list):
                raise TypeError('BaseConfigValue need value is list for id')
            self.multi_choices_value.set([
                i for i in BaseConfigItem.objects.filter(pk__in=value)
            ], clear=True)
            return
        if self.item.is_choices and not self.item.is_multiple_choices:
            try:
                self.choices_value = BaseConfigItem.objects.get(pk=value)
            except BaseConfigItem.DoesNotExist:
                raise ValueError('BaseConfigItem Does Not Exist!')
            return
        if not self.item or not self.item.item_type:
            raise TypeError('BaseConfigItem {0} does not set item_type'.format(self.item.pk))
        if self.item.item_type == 'str':
            self.str_value = str(value)
        elif self.item.item_type == 'bool':
            self.bool_value = bool(value)
        elif self.item.item_type in ['int', 'year']:
            self.int_value = int(value)
        elif self.item.item_type == 'float':
            self.float_value = float(value)
        elif self.item.item_type == 'decimal':
            self.decimal_value = Decimal(value)
        elif self.item.item_type == 'date':
            self.date_value = value
        elif self.item.item_type == 'datetime':
            self.datetime_value = value
        elif self.item.item_type == 'time':
            self.time_value = value
        elif self.item.item_type == 'file':
            self.file_value = value
        else:
            raise TypeError('BaseConfigItem {0} item_type error'.format(self.item.pk))

    value = property(get_value, set_value)

    @property
    def value_display(self):
        item = self.item
        if item.is_choices and item.is_multiple_choices:
            return list(self.multi_choices_value.all().values_list('name', flat=True))
        if item.is_choices and not item.is_multiple_choices:
            return self.choices_value.name if self.choices_value else None
        return self.value


class BaseConfigFileUpload(models.Model):
    file = models.FileField(
        '文件', upload_to='baseconfigvaluefile/%Y/%m/%d/', help_text='文件'
    )
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '基础配置项文件'
        verbose_name_plural = verbose_name
        ordering = ['pk']
