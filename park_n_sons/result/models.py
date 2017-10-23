from django.db import models

class Result(models.Model):
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
    PRICE = (
        (0, "Free"),
        (1, "Inexpensive"),
        (2, "Moderate"),
        (3, "Expensive"),
        (4, "Very Expensive"),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=None)
    type_business = models.IntegerField(default=None, choices=BUILDING)
    address = models.CharField(max_length=50, default=None)
    suburb = models.CharField(max_length=20, default=None)
    price = models.IntegerField(default=0, choices=PRICE)
    rating = models.FloatField(max_length=10, default=0.0)
    childFriendly = models.BooleanField(default=True)
    lat_coord = models.FloatField(max_length=10, default=None)
    long_coord = models.FloatField(max_length=10, default=None)

    def __str__(self):
        return self.name