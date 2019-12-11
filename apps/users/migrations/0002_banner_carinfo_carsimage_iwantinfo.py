# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-11 19:55
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='banner', verbose_name='轮播图片')),
                ('index', models.IntegerField(default=0, verbose_name='轮播顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '首页轮播',
                'verbose_name_plural': '首页轮播',
            },
        ),
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_image', models.ImageField(max_length=200, upload_to='car/images/%Y/%m/%d', verbose_name='主图')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('area', models.IntegerField(blank=True, choices=[(5, '翔安区'), (7, '龙文区'), (2, '集美区'), (1, '湖里区'), (4, '海沧区'), (0, '思明区'), (6, '芗城区'), (3, '杏林区')], null=True, verbose_name='地区')),
                ('car_type', models.IntegerField(blank=True, choices=[(3, '热门练手'), (1, '经典SUV'), (4, '超值低价'), (0, '面包车'), (2, '经济实用')], null=True, verbose_name='类型')),
                ('car_age', models.IntegerField(blank=True, choices=[(1, '1-3年'), (3, '5年以上'), (0, '1年以内'), (2, '3-5年')], null=True, verbose_name='年龄')),
                ('car_brand', models.IntegerField(blank=True, choices=[(1, '1-3年'), (3, '5年以上'), (0, '1年以内'), (2, '3-5年')], null=True, verbose_name='年龄')),
                ('car_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='售价')),
                ('car_origin_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='原价')),
                ('up_time', models.DateTimeField(blank=True, null=True, verbose_name='上牌时间')),
                ('car_km', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='里程数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_info', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='CarsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='car/images/%Y/%m/%d', verbose_name='图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_images', to='users.CarInfo', verbose_name='车详情图')),
            ],
            options={
                'verbose_name': '车详情图',
                'verbose_name_plural': '车详情图',
            },
        ),
        migrations.CreateModel(
            name='IWantInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('want_type', models.IntegerField(choices=[(0, '我要买车'), (1, '我要卖车')], verbose_name='类型')),
                ('name', models.CharField(max_length=15, verbose_name='姓名')),
                ('mobile', models.CharField(max_length=20, verbose_name='手机号')),
                ('brand', models.CharField(max_length=15, verbose_name='品牌')),
                ('desc', models.CharField(max_length=200, verbose_name='描述')),
                ('address', models.CharField(blank=True, max_length=20, null=True, verbose_name='你的地址')),
            ],
            options={
                'verbose_name': '预约表',
                'verbose_name_plural': '预约表',
            },
        ),
    ]
