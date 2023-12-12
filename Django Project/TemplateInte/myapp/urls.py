from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path('',views.index),
   path('about/',views.about),
   path('service/',views.service),
   path('team/',views.team),
   path('why/',views.why),
]