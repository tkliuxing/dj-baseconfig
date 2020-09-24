# Generated by Django 2.2.14 on 2020-07-21 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseconfig', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseconfigitem',
            name='sort_number',
            field=models.PositiveIntegerField(default=1, help_text='排序编号', verbose_name='排序编号'),
        ),
        migrations.AddField(
            model_name='baseconfigvalue',
            name='sort_number',
            field=models.PositiveIntegerField(default=1, help_text='排序编号', verbose_name='排序编号'),
        ),
    ]
