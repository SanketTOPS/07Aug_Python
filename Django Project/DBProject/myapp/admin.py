from django.contrib import admin
from .models import *

# Register your models here.
class userData(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','firstname','lastname','email','dob','address']

admin.site.register(userinfo,userData)