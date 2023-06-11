from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2) #3000.50
    unit = models.CharField(max_length=6)
