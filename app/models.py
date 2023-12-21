from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 24)
    password = models.CharField(max_length = 24)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10)


def create_account(name, username, password, email, phone_number):
    new_account = Account(
        name = name,
        username = username,
        password = password,
        email = email,
        phone_number = phone_number
    )
    new_account.save()
    return new_account


class Properties(models.Model):
    price = models.IntegerField()
    address = models.TextField()
    city = models.TextField()
    zip_code = models.IntegerField()
    size = models.IntegerField()
    available = models.BooleanField()