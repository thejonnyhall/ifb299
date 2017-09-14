from django.db import models

class Results(models.Model):
    BUILDING = (
        (0, "College"),
        (1, "Library"),
        (2, "Industry"),
        (3, "Hotel"),
        (4, "Park"),
        (5, "Zoo"),
        (6, "Museum"),
        (7, "Restaurant"),
        (8, "Mall"),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='NONE')
    type_business = models.IntegerField(default='NONE', choices=BUILDING)
    address = models.CharField(max_length=50, default='NONE')
    suburb = models.CharField(max_length=20, default='NONE')
    lat_coord = models.CharField(max_length=10, default='NONE')
    long_coord = models.CharField(max_length=10, default='NONE')