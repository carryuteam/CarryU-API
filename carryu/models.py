from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class User(models.Model):
    openid=models.CharField(max_length=50,primary_key=True)
    nickName=models.CharField(max_length=30)
    avatarUrl=models.URLField()
    description=models.TextField()
    create_time=models.DateTimeField(default=timezone.now)
    login_time=models.DateTimeField(default=timezone.now)
    school=models.CharField(max_length=20)
    grade=models.IntegerField()
    coin=models.IntegerField()


class Resource(models.Model):
    resid=models.AutoField(primary_key=True)
    author=models.CharField(max_length=50)
    resURL=models.URLField()
    school=models.CharField(max_length=20)
    grade=models.IntegerField() 
    picURLs=models.TextField()
    description=models.TextField()
    create_time=models.DateTimeField(default=timezone.now)
    update_time=models.DateTimeField(default=timezone.now)
    tags=models.TextField()
    cost=models.IntegerField()

class ResouceFolder(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    resid=models.ForeignKey(Resource,on_delete=models.CASCADE)
    class Meta:
        unique_together=("userid","resid")
    add_time=models.DateTimeField(default=timezone.now)
    comment=models.TextField()
