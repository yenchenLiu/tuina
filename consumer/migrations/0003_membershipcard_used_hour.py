# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0002_auto_20160402_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershipcard',
            name='used_hour',
            field=models.FloatField(default=0, verbose_name='hour'),
        ),
    ]
