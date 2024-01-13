from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('userlogin/',views.userlogin,name='userlogin'),
   path('home/',views.home,name='home'),
   path('userlogout/',views.userlogout),
   path('resetpass/',views.resetpass),
   path('newpass/',views.newpass,name='newpass'),
]
