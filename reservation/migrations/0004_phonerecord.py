# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20160512_1718'),
        ('reservation', '0003_auto_20160426_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('remark', models.TextField(blank=True, null=True, verbose_name='備註')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_record', to='user.CustomerPhone', verbose_name='電話')),
            ],
        ),
    ]
