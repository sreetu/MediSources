from typing import Optional
from django.db import models


# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200)
    pincode = models.IntegerField(null=True)
    deliver = models.BooleanField(default=True)
    dob = models.DateField()

    def __str__(self):
        return self.name

class Resource(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=100, default='bed')
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.provider.name + " " + self.provider.phone + " " + self.type
