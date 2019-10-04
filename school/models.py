from django.db import models

# Create your models here.
class School(models.Model):
    code=models.CharField(max_length=10,primary_key=True)
    schoolCode=models.CharField(max_length=10,default="NOCODE")
    schoolName=models.CharField(max_length=40)
    majorName=models.CharField(max_length=40)
