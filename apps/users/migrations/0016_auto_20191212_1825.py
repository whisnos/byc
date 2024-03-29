# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-12 18:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20191211_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarAgeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=15, verbose_name='车龄范围')),
                ('age_from', models.SmallIntegerField(blank=True, null=True, verbose_name='从')),
                ('age_to', models.SmallIntegerField(blank=True, null=True, verbose_name='到')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '车年龄范围',
                'verbose_name_plural': '车年龄范围',
            },
        ),
        migrations.AddField(
            model_name='carpriceinfo',
            name='price_from',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='从'),
        ),
        migrations.AddField(
            model_name='carpriceinfo',
            name='price_to',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='到'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='area',
            field=models.IntegerField(blank=True, choices=[(4, '海沧区'), (6, '芗城区'), (5, '翔安区'), (2, '集美区'), (0, '思明区'), (1, '湖里区'), (7, '龙文区'), (3, '杏林区')], null=True, verbose_name='地区'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_age',
            field=models.IntegerField(blank=True, choices=[(1, '1-3年'), (2, '3-5年'), (3, '5年以上'), (0, '1年以内')], null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='car_type',
            field=models.IntegerField(blank=True, choices=[(2, '经济实用'), (3, '热门练手'), (1, '经典SUV'), (0, '面包车'), (4, '超值低价')], null=True, verbose_name='类型'),
        ),
    ]
