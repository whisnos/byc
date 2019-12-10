from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
    # nick_name = models.CharField(max_length=20, verbose_name='用户昵称', null=True, blank=True)
    # image = models.ImageField(upload_to='user/%y/%m/%d', verbose_name='头像', max_length=200, null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    # is_start = models.BooleanField(default=False, verbose_name='是否激活')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

class CarInfo(models.Model):
    CHOICE_AREA={
        (0,'思明区'),
        (1, '湖里区'),
        (2, '集美区'),
        (3, '杏林区'),
        (4, '海沧区'),
        (5, '翔安区'),
        (6, '芗城区'),
        (7, '龙文区'),
    }
    CAR_TYPE={
        (0,'面包车'),
        (1, '经典SUV'),
        (2, '经济实用'),
        (3, '热门练手'),
        (4, '超值低价'),
    }
    CAR_AGE = {
        (0, '1年以内'),
        (1, '1-3年'),
        (2, '3-5年'),
        (3, '5年以上'),
    }
    CAR_BRAND = {
        (0, '大众'),
        (1, '丰田'),
        (2, '本田'),
        (3, '别克'),
    }
    title = models.CharField(max_length=50, verbose_name='标题')
    area= models.IntegerField(null=True, blank=True, choices=CHOICE_AREA, verbose_name='地区')
    car_type=models.IntegerField(null=True, blank=True, choices=CAR_TYPE, verbose_name='类型')
    car_age=models.IntegerField(null=True, blank=True, choices=CAR_AGE, verbose_name='年龄')
    car_brand=models.IntegerField(null=True, blank=True, choices=CAR_AGE, verbose_name='年龄')
    car_price=models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name='单价')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    # 上牌时间 里程KM