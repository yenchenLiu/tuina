# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0003_membershipcard_used_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipcard',
            name='used_hour',
            field=models.FloatField(default=0, verbose_name='used hour'),
        ),
    ]
