from django.db import models
# Create your models here.

class User(models.Model):
    user_id= models.AutoField(primary_key=True,unique=True) 
    name = models.CharField(max_length=32)
    email= models.EmailField(unique=True)
    membership_date = models.DateField()
