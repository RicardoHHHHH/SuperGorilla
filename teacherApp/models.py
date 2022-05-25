from django.db import models

# Create your models here.
class Teacher(models.Model):
    """教师表"""
    #Taccount = models.CharField(verbose_name="教师账号",max_length=255)
    password = models.CharField(verbose_name="密码", max_length=255)
    Ttunmb = models.CharField(verbose_name="教师号", max_length=255)
    phonenb = models.CharField(verbose_name="手机号", max_length=11)
    Tname = models.CharField(verbose_name="教师姓名", max_length=255)
    School = models.CharField(verbose_name="学校", max_length=255)