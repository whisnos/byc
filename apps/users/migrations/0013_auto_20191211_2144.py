# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-11 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20191211_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbrand',
            name='car_info',
        ),
        migrations.AddField(
            model_name='carinfo',
            name='car_brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.CarBrand', verbose_name='牌子'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='area',
            field=models.IntegerField(blank=True, choices=[(0, '思明区'), (2, '集美区'), (1, '湖里区'), (7, '龙文区'), (3, '杏林区'), (5, '翔安区'), (4, '海沧区'), (6, '芗城区')], null=True, verbose_name='地区'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_age',
            field=models.IntegerField(blank=True, choices=[(3, '5年以上'), (2, '3-5年'), (1, '1-3年'), (0, '1年以内')], null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_type',
            field=models.IntegerField(blank=True, choices=[(1, '经典SUV'), (0, '面包车'), (2, '经济实用'), (3, '热门练手'), (4, '超值低价')], null=True, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='iwantinfo',
            name='want_type',
            field=models.IntegerField(choices=[(0, '我要买车'), (1, '我要卖车')], verbose_name='类型'),
        ),
    ]
