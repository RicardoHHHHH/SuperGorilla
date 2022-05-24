# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Student(models.Model):
    """学生表"""
    #Saccount = models.CharField(verbose_name="学生账号",max_length=255)
    password = models.CharField(verbose_name="密码", max_length=255)
    Stunmb = models.CharField(verbose_name="学号", max_length=255)
    phonenb = models.CharField(verbose_name="手机号", max_length=11)
    Sname = models.CharField(verbose_name="学生姓名", max_length=255)
    School = models.CharField(verbose_name="学校", max_length=255)
