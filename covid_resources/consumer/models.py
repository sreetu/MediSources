from django.db import models

severity_choices = [('Mi', 'Mild'), ('Mo', 'Moderate'), ('C', 'Critical')]
# Create your models here.
class Consumer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    severity = models.CharField(max_length=50, choices=severity_choices, default='Mi')
    report = models.ImageField(upload_to='reports', null=True, blank=True)
    dob = models.DateField(null=True)

    def __str__(self):
        return self.name

class Request(models.Model):
    consumer = models.ForeignKey('Consumer', on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=100, default='bed')
    count = models.IntegerField(default=0)
    pending = models.BooleanField(default=False)
    completed = models.DateField()


