from django.contrib import admin
from .models import *

# Register your models here.


class userdata(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','role','firstname','lastname','username','city','state','mobile']

class studData(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','sub','branch']

admin.site.register(usersignup,userdata)
admin.site.register(stdata,studData)
