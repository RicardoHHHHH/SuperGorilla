import pymysql
import django.contrib

from studentApp import models
from studentApp.models import Student

student_queryset = models.Student.objects.all()
print(student_queryset)