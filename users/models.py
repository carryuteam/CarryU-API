#!coding=utf8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class UserManager(models.Manager):
    def get_by_natural_key(self, openid):
        return self.get(openid=openid)


class UserProfile(AbstractUser):
    openid = models.CharField("微信openid唯一标识符", max_length=50, primary_key=True)
    nickName = models.CharField("昵称", max_length=30, null=True)
    avatarUrl = models.URLField("头像链接", default="http://carryu.com", null=True)
    description = models.TextField("描述信息", default="")
    create_time = models.DateTimeField("创建时间", default=timezone.now)
    login_time = models.DateTimeField("上次登陆时间", default=timezone.now)
    school = models.IntegerField("学院", null=True)
    gender = models.IntegerField("性别", default=2)
    grade = models.IntegerField("年级", null=True)
    coin = models.IntegerField("金币", default=10)
    sessionKey = models.TextField("SessionKey")
    password = models.TextField('供admin登陆密码')
    username=models.TextField('复写先前的username')
    USERNAME_FIELD = 'openid'
    objects = UserManager()

