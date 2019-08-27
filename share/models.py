from django.db import models
from django.utils import timezone


class ShareModel(models.Model):
    id = models.AutoField("帖子ID", primary_key=True)
    uid = models.CharField("发帖人OpenID", max_length=50)
    create_time = models.DateTimeField("创建时间", default=timezone.now)

    title = models.CharField("帖子标题", max_length=50)
    content = models.TextField("帖子内容")

    comment = models.IntegerField("评论总数", default=0)
    like = models.IntegerField("点赞总数", default=0)
    store = models.IntegerField("收藏总数", default=0)


class ShareComment(models.Model):  # 评论
    id = models.AutoField("评论ID", primary_key=True)
    uid = models.CharField("评论人OpenID", max_length=50)
    sid = models.IntegerField("帖子ID")
    comment = models.CharField("评论内容", max_length=200)
    create_time = models.DateTimeField("创建时间", default=timezone.now)


class ShareLike(models.Model):  # 点赞
    id = models.AutoField("评论ID", primary_key=True)
    uid = models.CharField("评论人OpenID", max_length=50)
    sid = models.IntegerField("帖子ID")
    create_time = models.DateTimeField("创建时间", default=timezone.now)


class ShareStore(models.Model):  # 收藏
    id = models.AutoField("评论ID", primary_key=True)
    uid = models.CharField("评论人OpenID", max_length=50)
    sid = models.IntegerField("帖子ID")
    create_time = models.DateTimeField("创建时间", default=timezone.now)
