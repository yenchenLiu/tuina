# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-26 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0010_auto_20160402_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipcard',
            name='number',
            field=models.IntegerField(verbose_name='number'),
        ),
    ]
