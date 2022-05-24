from django.urls import path, include
from studentApp import views

urlpatterns = [
    path('index/', views.index),
    path('studentRegister/', views.studentRegister)
]