from unicodedata import decimal
from django.db import models

# Create your models here.

class MyWatchlist(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=5, decimal_places=1)
    release_date = models.DateField()
    review = models.TextField()