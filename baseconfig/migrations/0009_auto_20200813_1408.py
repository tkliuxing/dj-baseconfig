# Generated by Django 2.2.14 on 2020-08-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseconfig', '0008_baseconfigcategory_is_choice_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseConfigFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='文件', upload_to='baseconfigvaluefile/%Y/%m/%d/', verbose_name='文件')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '基础配置项文件',
                'verbose_name_plural': '基础配置项文件',
                'ordering': ['pk'],
            },
        ),
        migrations.AlterModelOptions(
            name='baseconfigitem',
            options={'ordering': ['category', 'sort_number', 'pk'], 'verbose_name': '基础配置项定义', 'verbose_name_plural': '基础配置项定义'},
        ),
    ]
