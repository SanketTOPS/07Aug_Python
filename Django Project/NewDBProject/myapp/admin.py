from django.contrib import admin
from .models import *

# Register your models here.

class userData(admin.ModelAdmin):
    list_display=['firstname','lastname','email','dob','city']

admin.site.register(userInfo,userData)