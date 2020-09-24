# Generated by Django 2.2.14 on 2020-08-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseconfig', '0006_baseconfigitem_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseconfigvalue',
            name='file_value',
            field=models.TextField(blank=True, null=True, verbose_name='文件URL'),
        ),
        migrations.AlterField(
            model_name='baseconfigitem',
            name='item_type',
            field=models.CharField(choices=[('str', '字符串'), ('bool', '布尔值'), ('int', '整数'), ('float', '浮点数'), ('decimal', '精确浮点数'), ('date', '日期'), ('datetime', '日期时间'), ('time', '时间'), ('file', '文件')], default='str', max_length=20, verbose_name='配置项类型'),
        ),
    ]
