from django.db import models

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    propic=models.FileField(upload_to="user_profile/",default="defaultuser.png")
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.email