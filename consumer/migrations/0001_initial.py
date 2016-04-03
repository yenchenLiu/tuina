# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0010_customer_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True, unique=True, verbose_name='number')),
                ('category', models.CharField(choices=[('一般', '一般'), ('深層推拿', '深層推拿')], max_length=45, verbose_name='category')),
                ('hour', models.FloatField(verbose_name='hour')),
                ('total_money', models.IntegerField(verbose_name='total money')),
                ('payment_method', models.CharField(choices=[('現金', '現金'), ('刷卡', '刷卡')], max_length=20, verbose_name='payment method')),
                ('amount_paid', models.IntegerField(default=0, verbose_name='amount paid')),
                ('remark', models.TextField(default=True, null=True, verbose_name='remark')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_card', to='user.Customer', verbose_name='customer')),
            ],
            options={
                'verbose_name_plural': '會員卡資料',
                'verbose_name': '會員卡資料',
            },
        ),
    ]
