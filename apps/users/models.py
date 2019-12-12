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


class CarBrand(models.Model):
    name = models.CharField(max_length=15, verbose_name='名字')
    first_letter = models.CharField(null=True, blank=True, max_length=5, verbose_name='首字符')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '品牌管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CarPriceInfo(models.Model):
    price = models.CharField(max_length=15, verbose_name='价格范围')
    price_from = models.SmallIntegerField(null=True, blank=True, verbose_name='从')
    price_to = models.SmallIntegerField(null=True, blank=True, verbose_name='到')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '价格范围'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.price


class CarAgeInfo(models.Model):
    age = models.CharField(max_length=15, verbose_name='车龄范围')
    age_from = models.SmallIntegerField(null=True, blank=True, verbose_name='从')
    age_to = models.SmallIntegerField(null=True, blank=True, verbose_name='到')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '车年龄范围'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.price


class CarInfo(models.Model):
    CHOICE_AREA = {
        (0, '思明区'),
        (1, '湖里区'),
        (2, '集美区'),
        (3, '杏林区'),
        (4, '海沧区'),
        (5, '翔安区'),
        (6, '芗城区'),
        (7, '龙文区'),
    }
    CAR_TYPE = {
        (0, '面包车'),
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

    user = models.ForeignKey(UserProfile, related_name='car_info', on_delete=models.CASCADE, verbose_name='用户')
    car_image = models.ImageField(null=True, blank=True, max_length=200, upload_to="car/images/%Y/%m/",
                                  verbose_name='主图')
    title = models.CharField(max_length=50, verbose_name='标题')
    area = models.IntegerField(null=True, blank=True, choices=CHOICE_AREA, verbose_name='地区')
    car_type = models.IntegerField(null=True, blank=True, choices=CAR_TYPE, verbose_name='类型')
    car_age = models.IntegerField(null=True, blank=True, choices=CAR_AGE, verbose_name='年龄')
    car_brand = models.ForeignKey(CarBrand, null=True, blank=True, verbose_name='牌子')
    car_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='售价')
    car_origin_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='原价')
    up_time = models.DateTimeField(null=True, blank=True, verbose_name='上牌时间')
    car_km = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2, verbose_name='里程数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')

    # 上牌时间 里程KM
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '车信息管理'
        verbose_name_plural = verbose_name


class CarsImage(models.Model):
    """
    车详情图
    """
    car = models.ForeignKey(CarInfo, verbose_name="车详情图", related_name="car_images")
    image = models.ImageField(max_length=200, upload_to="car/images/%Y/%m/", verbose_name="图片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "车详情图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.car.title


class IWantInfo(models.Model):
    WANT_TYPE = {
        (0, '我要买车'),
        (1, '我要卖车'),
    }
    want_type = models.IntegerField(choices=WANT_TYPE, verbose_name='类型')
    name = models.CharField(max_length=15, verbose_name='姓名')
    mobile = models.CharField(max_length=20, verbose_name='手机号')
    brand = models.CharField(max_length=15, verbose_name='品牌')
    desc = models.CharField(max_length=200, verbose_name='描述')
    address = models.CharField(null=True, blank=True, max_length=20, verbose_name='你的地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "预约表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Banner(models.Model):
    """
    首页轮播
    """
    image = models.ImageField(max_length=200, upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '首页轮播'
        verbose_name_plural = verbose_name

        # def __str__(self):
        #     return self.image
