from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class ResouceTag(models.Model):
    tag = models.CharField("tag名称",max_length=40, primary_key=True)
    #此处会有自增主键

class Resource(models.Model):
    resid=models.AutoField(primary_key=True)
    author=models.CharField(max_length=50)
    name=models.CharField(max_length=50,default="res")
    resURL=models.CharField(max_length=100)
    school=models.CharField(max_length=20)
    grade=models.IntegerField()
    picURLs=models.TextField()
    description=models.TextField()
    create_time=models.DateTimeField(default=timezone.now)
    update_time=models.DateTimeField(default=timezone.now)
    tags=models.TextField()
    cost=models.IntegerField()
    score=models.FloatField(default=4.5)


class ResouceFolder(models.Model):
    userid=models.TextField()
    #注意这里user没有和真正的user连起来！
    resid=models.TextField()
    add_time=models.DateTimeField(default=timezone.now)
    comment=models.TextField()
    is_buy=models.IntegerField(default=0)
    class Meta:
        unique_together=("userid","resid")

'''
class Course(models.Model):
    id=models.CharField(max_length=30)
    name=models.TextField()
    school=models.CharField(max_length=20)
    grade=models.IntegerField()
'''

class ResouceDic(models.Model):
    dicid=models.AutoField("文件夹id",primary_key = True)
    userid=models.TextField("user的openid")
    name=models.TextField("文件夹名字")
    parent=models.TextField("父级目录id")

class ResouceComment(models.Model):
    #这里会有个自增的id
    userid=models.CharField(max_length=50)
    resid=models.CharField(max_length=50)
    content=models.TextField()
    score=models.FloatField()#满分5分
    create_time=models.DateTimeField(default=timezone.now)





