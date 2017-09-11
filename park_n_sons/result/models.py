from django.db import models

# Create your models here.
class Results(models.Model):
    name = models.CharField(max_length=20, default='NONE')
    type_business = models.CharField(max_length=20, default='NONE')
    address = models.CharField(max_length=50, default='NONE')
    suburb = models.CharField(max_length=20, default='NONE')
    lat_coord = models.CharField(max_length=10, default='NONE')
    long_coord = models.CharField(max_length=10, default='NONE')