from django.db import models

severity_choices = [('Mi', 'Mild'), ('Mo', 'Moderate'), ('C', 'Critical')]
# Create your models here.
class Consumer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    severity = models.CharField(max_length=50, choices=severity_choices, default='Mi')
    report = models.ImageField(upload_to='reports')

    def __str__(self):
        return self.name
