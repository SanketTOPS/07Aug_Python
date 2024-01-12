from django.db import models

# Create your models here.


class usersignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    role=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class stdata(models.Model):
    sub=models.CharField(max_length=20)
    branch=models.CharField(max_length=20)

