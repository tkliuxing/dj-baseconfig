# Generated by Django 2.2.15 on 2020-08-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseconfig', '0009_auto_20200813_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseconfigvalue',
            name='raw_value',
            field=models.TextField(blank=True, help_text='原始值', null=True, verbose_name='原始值'),
        ),
    ]
