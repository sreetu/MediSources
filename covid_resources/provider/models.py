from django.db import models

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pincode = models.IntegerField(null=True)
    deliver = models.BooleanField(default=True)
    dob = models.DateField()

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100,default=None,null=True,blank=True)

    def __str__(self):
        if self.type:
            return self.name+" "+self.type
        else:
            return self.name

