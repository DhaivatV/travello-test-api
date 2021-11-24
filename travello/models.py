from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

class Destination(models.Model):
    name = models.CharField(max_length=100)
    descr = models.TextField()
    image = models.ImageField(upload_to= 'pics')
    price = models.IntegerField()
    offers = models.BooleanField(default=False)
    rating = models.IntegerField()

class UpcomingOffers (models.Model):
    Place = models.CharField(max_length=100)
    decr = models.CharField(max_length= 100)
    pic = models.ImageField(upload_to='photos')
    amt = models.FloatField()
    offr = models.CharField(max_length=100)
    ratings = models.IntegerField()
