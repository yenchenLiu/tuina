# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20160402_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='age'),
        ),
    ]
