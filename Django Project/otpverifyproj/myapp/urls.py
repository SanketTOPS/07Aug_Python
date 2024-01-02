from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.login,name='login'),
    path('signup/',views.signup),
    path('home/',views.home),
    path('otpverify/',views.otpverify,name='otpverify'),
]
