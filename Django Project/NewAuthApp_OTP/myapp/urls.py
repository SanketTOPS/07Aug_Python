from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('home',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('otp/',views.otp,name='otp'),
    path('login/',views.login,name='login'),
]
