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