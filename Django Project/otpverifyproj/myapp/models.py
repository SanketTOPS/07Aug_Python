from django.db import models
from datetime import datetime

# Create your models here.


class newuser(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    mobile=models.BigIntegerField()