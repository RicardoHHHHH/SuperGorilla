from django.db import models

# Create your models here.
class Student(models.Model):
    """学生表"""
    #Saccount = models.CharField(verbose_name="学生账号",max_length=255)
    password = models.CharField(verbose_name="密码", max_length=255)
    Stunmb = models.CharField(verbose_name="学号", max_length=255)
    phonenb = models.CharField(verbose_name="手机号", max_length=11)
    Sname = models.CharField(verbose_name="学生姓名", max_length=255)
    School = models.CharField(verbose_name="学校", max_length=255)