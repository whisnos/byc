# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-11 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191211_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinfo',
            name='area',
            field=models.IntegerField(blank=True, choices=[(3, '杏林区'), (1, '湖里区'), (6, '芗城区'), (7, '龙文区'), (4, '海沧区'), (2, '集美区'), (0, '思明区'), (5, '翔安区')], null=True, verbose_name='地区'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_age',
            field=models.IntegerField(blank=True, choices=[(0, '1年以内'), (2, '3-5年'), (1, '1-3年'), (3, '5年以上')], null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_brand',
            field=models.IntegerField(blank=True, choices=[(0, '大众'), (3, '别克'), (2, '本田'), (1, '丰田')], null=True, verbose_name='牌子'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_image',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='car/images/main/', verbose_name='主图'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_type',
            field=models.IntegerField(blank=True, choices=[(0, '面包车'), (4, '超值低价'), (3, '热门练手'), (2, '经济实用'), (1, '经典SUV')], null=True, verbose_name='类型'),
        ),
    ]
