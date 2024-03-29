# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 09:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20160512_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerphone',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='電話號碼必須是純數字，上限為15個字。例如+8861234567,021234567', regex='^\\+?\\d{5,15}$')], verbose_name='電話號碼'),
        ),
    ]
