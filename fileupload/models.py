from django.db import models
from django.utils import timezone
# Create your models here.


class UploadModel(models.Model):
    id = models.AutoField("文件ID", primary_key=True)
    uid = models.CharField("上传人OpenID", max_length=50)
    create_time = models.DateTimeField("创建时间", default=timezone.now)
    src = models.TextField("文件地址")
