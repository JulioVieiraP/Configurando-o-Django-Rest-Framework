from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
