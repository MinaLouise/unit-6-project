from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length = 24)
    username = models.CharField(max_length = 24)
    password = models.CharField(max_length = 24)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)



class Properties(models.Model):
    price = models.IntegerField()
    address = models.TextField()
    city = models.TextField()
    zip_code = models.IntegerField()
    size = models.IntegerField()
    available = models.BooleanField()








# class User(models.Model):
#     name = models.CharField(max_length = 24)
#     username = models.CharField(max_length = 24)
#     password = models.CharField(max_length = 255)
#     email = models.EmailField()
#     number = models.CharField(max_length = 10)
