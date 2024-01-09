from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length = 24)
    phone_number = models.CharField(max_length = 10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Properties(models.Model):
    user_props = models.ForeignKey(Account, on_delete=models.CASCADE)
    price = models.IntegerField()
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    zip_code = models.IntegerField()
    size = models.IntegerField()
    available = models.BooleanField()
    picture = models.ImageField(null=True, blank=True)


