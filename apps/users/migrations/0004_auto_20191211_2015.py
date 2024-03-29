# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-11 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191211_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinfo',
            name='area',
            field=models.IntegerField(blank=True, choices=[(2, '集美区'), (5, '翔安区'), (0, '思明区'), (6, '芗城区'), (4, '海沧区'), (7, '龙文区'), (3, '杏林区'), (1, '湖里区')], null=True, verbose_name='地区'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_age',
            field=models.IntegerField(blank=True, choices=[(3, '5年以上'), (1, '1-3年'), (2, '3-5年'), (0, '1年以内')], null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_brand',
            field=models.IntegerField(blank=True, choices=[(0, '大众'), (1, '丰田'), (2, '本田'), (3, '别克')], null=True, verbose_name='牌子'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_image',
            field=models.ImageField(max_length=200, upload_to='car/images/main', verbose_name='主图'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_type',
            field=models.IntegerField(blank=True, choices=[(1, '经典SUV'), (4, '超值低价'), (0, '面包车'), (2, '经济实用'), (3, '热门练手')], null=True, verbose_name='类型'),
        ),
    ]
