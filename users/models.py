#!coding=utf8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class UserManager(models.Manager):
    def create_user(self, username, password=None, email=None):
        """
        Creates and saves a User with the given 
        user name and password.
        """
        if not username:
            raise ValueError(_('Users must have an username'))
 
        user = self.model(
            username=username,
        )
 
        user.set_password(password)
        user.is_admin = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email):
        """
        Creates and saves a superuser with the given  
        user name and password.
        """
        user = self.create_user(
            password=password,
            username=username
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
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
    gender = models.CharField(
        max_length=6,
        choices=(
            ('male', '男'),
            ('female', '女'),
            ('other', '其他')
        ),
        default='other'
    )
    grade = models.IntegerField("年级", null=True)
    coin = models.IntegerField("金币", default=10)
    sessionKey = models.TextField("SessionKey")
    password = models.TextField('供admin登陆密码')

    objects = UserManager()

