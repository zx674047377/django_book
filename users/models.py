from datetime import datetime

from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    APIkey = models.CharField(verbose_name="APIkey", max_length=30, default="abcdefghijklmn")
    money = models.IntegerField(verbose_name="余额", default=10)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Book(models.Model):
    """书籍信息"""
    title = models.CharField(verbose_name="书名", max_length=30)
    isbn = models.CharField(verbose_name="isbn", max_length=30, default=" ")
    author = models.CharField(verbose_name="作者", max_length=20, default=" ")
    publish = models.CharField(verbose_name="出版社", max_length=50, default=" ")
    rate = models.FloatField(verbose_name="评分", default=0)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "书籍信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
