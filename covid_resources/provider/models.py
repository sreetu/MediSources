from django.db import models

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    startingTime = models.CharField(max_length=10)
    endingTime = models.CharField(max_length=10)
    homeDelivery = models.BooleanField(default=True)
    callDuration = models.CharField(max_length=10)
    available = models.BooleanField(default=True)
    bed = models.IntegerField(default=0)
    oxygenCylinder = models.IntegerField(default=0)
    oxygenCylinderToolkit = models.IntegerField(default=0)
    homeIsolationKit = models.IntegerField(default=0)


