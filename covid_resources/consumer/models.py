from django.db import models

# Create your models here.
class Consumer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    severity = models.CharField(max_length=50)
    report = models.ImageField()