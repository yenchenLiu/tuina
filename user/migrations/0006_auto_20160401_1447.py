# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20160401_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': '顧客資料', 'verbose_name_plural': '顧客資料'},
        ),
        migrations.AddField(
            model_name='customer',
            name='number',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='number'),
        ),
    ]
