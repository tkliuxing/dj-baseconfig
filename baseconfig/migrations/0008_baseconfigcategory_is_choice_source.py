# Generated by Django 2.2.14 on 2020-08-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseconfig', '0007_auto_20200813_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseconfigcategory',
            name='is_choice_source',
            field=models.BooleanField(default=False, help_text='选项类型字段数据源', verbose_name='选项类型字段数据源'),
        ),
    ]